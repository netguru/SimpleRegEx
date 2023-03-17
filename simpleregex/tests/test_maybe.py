# -*- coding: utf-8 -*-
from simpleregex.func import maybe


class TestMaybe:
    def test_none(self):
        assert maybe("a").compile().match("bbb")

    def test_one(self):
        re_match = maybe("a").compile().search("abbb")
        assert re_match[0] == "a"

    def test_many(self):
        re_match = maybe("a").compile().search("aaabbb")
        assert re_match[0] == "a"
