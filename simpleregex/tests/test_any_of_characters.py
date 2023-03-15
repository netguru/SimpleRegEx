# -*- coding: utf-8 -*-
from simpleregex.func import any_of_characters


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
