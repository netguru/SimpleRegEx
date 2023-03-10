# -*- coding: utf-8 -*-
from simpleregex.func import none_or_many


class TestNoneOrMany:
    def test_none(self):
        assert none_or_many("a").compile().match("bbb")

    def test_one(self):
        re_match = none_or_many("a").compile().search("abbb")
        assert re_match[0] == "a"

    def test_many(self):
        re_match = none_or_many("a").compile().search("aaabbb")
        assert re_match[0] == "aaa"
