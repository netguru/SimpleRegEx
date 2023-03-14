# -*- coding: utf-8 -*-
from simpleregex.func import any_of_char


class TestAnyOfChar:
    def test_none(self):
        assert not any_of_char("a").compile().match("bbb")

    def test_one(self):
        re_match = any_of_char("a").compile().search("abbb")
        assert re_match[0] == "a"

    def test_many(self):
        re_match = any_of_char("ab").compile().search("ZzAbaaabbbaaa")
        assert re_match[0] == "b"
