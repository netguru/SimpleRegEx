# -*- coding: utf-8 -*-
from simpleregex.func import noneOrMany


class TestNoneormany:
    def test_none(self):
        assert noneOrMany("a").compile().match("bbb")

    def test_one(self):
        match = noneOrMany("a").compile().search("abbb")
        assert match[0] == "a"

    def test_many(self):
        match = noneOrMany("a").compile().search("aaabbb")
        assert match[0] == "aaa"
