# -*- coding: utf-8 -*-
from simpleregex.func import any_of_characters
from simpleregex.func import regex_range
from simpleregex.models import RegEx


class TestAnyOfChar:
    def test_none(self):
        assert not any_of_characters(["a"]).compile().match("bbb")

    def test_one(self):
        re_match = any_of_characters(["a"]).compile().search("abbb")
        assert re_match[0] == "a"

    def test_many(self):
        re_match = (
            any_of_characters(["a", "b"]).compile().search("ZzAbaaabbbaaa")
        )
        assert re_match[0] == "b"

    def test_string(self):
        """
        any_of_characters should also except string instead of list
        """
        re_match = any_of_characters("ab").compile().search("ZzAbaaabbbaaa")
        assert re_match[0] == "b"

    def test_with_regex_range(self):
        """
        any_of_characters should also except regex range object
        """
        regex = any_of_characters(
            [
                regex_range("a", "z"),
                regex_range(
                    0,
                    9,
                ),
                "-",
            ]
        ).compile()

        assert regex.pattern == "[a-z0-9-]"

        re_match = regex.search("ZzAbaaabbbaaa")
        assert re_match[0] == "z"

    def test_with_regex_object(self):
        """
        any_of_characters should also except regex object
        """
        regex = any_of_characters(
            [RegEx("a-z"), RegEx(["0", "-", "9"]), "-"]
        ).compile()

        assert regex.pattern == "[a-z0-9-]"

        re_match = regex.search("ZzAbaaabbbaaa")
        assert re_match[0] == "z"
