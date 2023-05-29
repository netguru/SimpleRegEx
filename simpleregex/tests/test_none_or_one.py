# -*- coding: utf-8 -*-
from simpleregex.func import none_or_one


class TestNoneOrOne:
    def test_none(self):
        assert not none_or_one("a").compile().match("bbb").group()

    def test_one(self):
        re_match = none_or_one("a").compile().search("abbb")
        assert re_match[0] == "a"

    def test_many(self):
        re_match = none_or_one("a").compile().search("aaabbb")
        assert re_match[0] == "a"
