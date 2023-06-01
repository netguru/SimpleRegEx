# -*- coding: utf-8 -*-
from simpleregex.func import none_or_many


class TestNoneOrMany:
    def test_none(self):
        assert not none_or_many("a").compile().match("bbb").group()

    def test_one(self):
        re_match = none_or_many("a").compile().search("abbb")

        assert re_match[0] == "a"

        re_match = none_or_many("foo").compile().search("foobar")

        assert re_match[0] == "foo"

    def test_many(self):
        re_match = none_or_many("a").compile().search("aaabbb")
        assert re_match[0] == "aaa"

        re_match = none_or_many("foo").compile().search("foofoobarbar")
        assert re_match[0] == "foofoo"
