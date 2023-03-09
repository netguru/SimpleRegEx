# -*- coding: utf-8 -*-
from SimpleRegEx.func import oneOrMore


class TestOneormore:
    def test_none(self):
        assert not oneOrMore("a").compile().match("bbb")

    def test_one(self):
        match = oneOrMore("a").compile().search("abbb")
        assert match[0] == "a"

    def test_many(self):
        match = oneOrMore("a").compile().search("aaabbb")
        assert match[0] == "aaa"
