# -*- coding: utf-8 -*-
import re
from dataclasses import dataclass

from simpleregex.func import any_of_characters
from simpleregex.func import group
from simpleregex.func import none_or_many
from simpleregex.func import none_or_one
from simpleregex.func import one_or_more
from simpleregex.func import regex_or
from simpleregex.func import regex_range
from simpleregex.func import times
from simpleregex.models import RegEx


@dataclass
class EmailAddressPattern:
    @property
    def allowed_chars(self):
        """
        Characters allowed for local alphanumeric part.
        """
        return one_or_more(
            any_of_characters(
                [
                    regex_range("a", "z"),
                    regex_range("0", "9"),
                    "_",
                    "!",
                    "#",
                    "$",
                    "%",
                    "&",
                    "'",
                    "*",
                    "+",
                    "\\",
                    "/",
                    "=",
                    "?",
                    "^",
                    "`",
                    "{",
                    "|",
                    "}",
                    "~",
                    "-",
                ]
            )
        )

    @property
    def local_alphanumeric(self):
        """
        Local alphanumeric part regex.
        """
        return none_or_many(
            self.allowed_chars
            + group(RegEx("\.") + self.allowed_chars, non_capturing=True)
        )

    @property
    def domain_alphanumeric(self):
        """
        Alphanumeric regex for the domain part.
        """
        lower_alphanumeric = any_of_characters(
            [regex_range("a", "z"), regex_range("0", "9")]
        )
        lower_alphanumeric_dash = any_of_characters(
            [regex_range("a", "z"), regex_range("0", "9"), "-"]
        )
        return (
            one_or_more(
                group(
                    lower_alphanumeric
                    + none_or_one(
                        group(
                            none_or_many(lower_alphanumeric_dash)
                            + lower_alphanumeric,
                            non_capturing=True,
                        )
                    )
                    + RegEx("\\."),
                    non_capturing=True,
                )
            )
            + lower_alphanumeric
            + none_or_one(
                group(
                    none_or_many(lower_alphanumeric_dash) + lower_alphanumeric,
                    non_capturing=True,
                )
            )
        )

    @property
    def local_allowed_special_chars(self):
        """
        Special ascii characters allowed in local part.
        """
        return any_of_characters(
            [
                regex_range(r"\x01", r"\x08"),
                r"\x0b",
                r"\x0c",
                regex_range(r"\x0e", r"\x1f"),
                r"\x21",
                regex_range(r"\x23", r"\x5b"),
                regex_range(r"\x5d", r"\x7f"),
            ]
        )

    @property
    def domain_allowed_special_chars(self):
        """
        Special ascii characters allowed in domain part.
        """
        return any_of_characters(
            [
                regex_range(r"\x01", r"\x08"),
                r"\x0b",
                r"\x0c",
                regex_range(r"\x0e", r"\x1f"),
                regex_range(r"\x21", r"\x5a"),
                regex_range(r"\x53", r"\x7f"),
            ]
        )

    @property
    def chars_allowed_after_backslash(self):
        """
        Special ascii characters allowed in local and domain part,
        only if prefixed with a backslash.
        """
        return RegEx("\\") + any_of_characters(
            [
                regex_range(r"\x01", r"\x09"),
                r"\x0b",
                r"\x0c",
                regex_range(r"\x0e", r"\x7f"),
            ]
        )

    @property
    def local_allowed_quoted_string(self):
        """
        Pattern for special characters allowed in local part.
        """
        return (
            RegEx('\\"')
            + none_or_many(
                group(
                    regex_or(
                        [
                            self.local_allowed_special_chars,
                            self.chars_allowed_after_backslash,
                        ]
                    ),
                    non_capturing=True,
                )
            )
            + RegEx('\\"')
        )

    @property
    def local_part(self):
        """
        Regex expression to mach local part of the email.
        Everything before "@" sign.
        """
        return group(
            regex_or(
                [self.local_alphanumeric, self.local_allowed_quoted_string]
            ),
            non_capturing=True,
        )

    @property
    def ip_bit(self):
        return regex_or(
            [
                RegEx("25") + regex_range(0, 5),
                RegEx("2") + regex_range(0, 4) + regex_range(0, 9),
                none_or_one(
                    none_or_one(any_of_characters(["0", "1"]))
                    + regex_range(0, 9)
                    + regex_range(0, 9)
                ),
            ]
        )

    @property
    def ip_network_id_pattern(self):
        """
        First three parts of the ip number.
        """
        return times(
            group(
                group(self.ip_bit, non_capturing=True) + RegEx("\\."),
                non_capturing=True,
            ),
            3,
        )

    @property
    def ip_device_id_pattern(self):
        """
        Last parts of the ip number.
        Can contain special characters, port number, device name etc.
        """
        return group(
            self.ip_bit
            + RegEx("|")
            + none_or_many(
                any_of_characters(
                    [regex_range("a", "z"), regex_range("0", "9"), "-"]
                )
            )
            + any_of_characters([regex_range("a", "z"), regex_range("0", "9")])
            + RegEx(":")
            + one_or_more(
                group(
                    regex_or(
                        [
                            self.domain_allowed_special_chars,
                            self.chars_allowed_after_backslash,
                        ]
                    ),
                    non_capturing=True,
                )
            ),
            non_capturing=True,
        )

    @property
    def base_ipv4_pattern(self):
        return self.ip_network_id_pattern + self.ip_device_id_pattern

    @property
    def domain_ip_part(self):
        return RegEx("\\[") + self.base_ipv4_pattern + RegEx("\\]")

    @property
    def domain_part(self):
        """
        Pattern to match everything after the @ sign.
        """
        return group(
            regex_or([self.domain_alphanumeric, self.domain_ip_part]),
            non_capturing=True,
        )

    @property
    def email_address_pattern(self):
        return self.local_part + RegEx("@") + self.domain_part


def test_local_part_alphanumeric():
    re_match = (
        EmailAddressPattern()
        .local_part.compile()
        .match("example.mail@gmail.com")
    )
    assert re_match.group() == "example.mail"


def test_local_part_special_characters():
    regex = EmailAddressPattern().local_allowed_quoted_string.compile()
    re_match = regex.match('"example\x08mail"@gmail.com')
    assert re_match.group() == '"example\x08mail"'


def test_local_part_special_characters_not_allowed_char():
    regex = EmailAddressPattern().local_allowed_quoted_string.compile()
    assert regex.match('"empty\x00void"@gmail.com') is None


def test_domain_part_alphanumeric():
    re_match = (
        EmailAddressPattern().domain_alphanumeric.compile().match("gmail.com")
    )
    assert re_match.group() == "gmail.com"


def test_base_ipv4_pattern():
    re_match = (
        EmailAddressPattern().base_ipv4_pattern.compile().match("255.255.255.0")
    )
    assert re_match.group() == "255.255.255.0"


def test_domain_ip_part():
    re_match = (
        EmailAddressPattern().domain_ip_part.compile().match("[192.168.0.1:25]")
    )
    assert re_match.group() == "[192.168.0.1:25]"


def test_domain_part():
    pattern = EmailAddressPattern().domain_part.compile()

    re_match = pattern.match("gmail.com")
    assert re_match.group() == "gmail.com"

    re_match = pattern.match("[192.168.0.1:25]")
    assert re_match.group() == "[192.168.0.1:25]"


def test_email_address_pattern():
    pattern = EmailAddressPattern().email_address_pattern.compile(
        flags=re.IGNORECASE
    )

    re_match = pattern.match("example.mail@gmail.com")
    assert re_match.group() == "example.mail@gmail.com"

    re_match = pattern.match('"example\x08mail"@[192.168.0.1:25]')
    assert re_match.group() == '"example\x08mail"@[192.168.0.1:25]'
