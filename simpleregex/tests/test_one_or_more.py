# -*- coding: utf-8 -*-
from simpleregex.func import one_or_more


class TestoneOrMore:
    def test_none(self):
        assert not one_or_more("a").compile().match("bbb")

    def test_one(self):
        re_match = one_or_more("a").compile().search("abbb")

        assert re_match[0] == "a"

        re_match = one_or_more("foo").compile().search("foobar")

        assert re_match[0] == "foo"

    def test_many(self):
        re_match = one_or_more("a").compile().search("aaabbb")

        assert re_match[0] == "aaa"

        re_match = one_or_more("foo").compile().search("foofoobarbar")

        assert re_match[0] == "foofoo"
