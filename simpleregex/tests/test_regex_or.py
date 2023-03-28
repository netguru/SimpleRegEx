# -*- coding: utf-8 -*-
from simpleregex.func import group
from simpleregex.func import regex_or
from simpleregex.models import RegEx


class TestRegexOr:
    def test_regex_or_multiple_groups(self):
        regex = regex_or([group("Lorem"), group("Ipsum"), "Donor"]).compile()

        assert regex.pattern == "(Lorem)|(Ipsum)|Donor"

        re_match = regex.match("Lorem Ipsum Donor")
        assert re_match is not None
        assert re_match[0] == "Lorem"

    def test_regex_or_multiple_groups_no_result(self):
        regex = regex_or(["Sit", "Amet", "Consectetur"]).compile()

        assert regex.pattern == "Sit|Amet|Consectetur"

        match = regex.match("Lorem Ipsum Donor")
        assert match is None

    def test_regex_or_multiple_groups_after_string(self):
        regex = (
            RegEx("Lorem ") + group(regex_or(["Ipsum", "Donor"]))
        ).compile()

        assert regex.pattern == "Lorem (Ipsum|Donor)"

        re_match = regex.match("Lorem Donor Ipsum")
        assert re_match[0] == "Lorem Donor"
