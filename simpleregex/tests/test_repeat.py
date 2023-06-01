# -*- coding: utf-8 -*-
from simpleregex.func import repeat


class TestRepeat:
    def test_when_provided_not_matched(self):
        assert not repeat("a", 2).compile().match("aba")
        assert not repeat("foo", 2).compile().match("foobar")

    def test_when_matched(self):
        assert repeat("a", 2).compile().match("aaba")
        assert repeat("a", 2).compile().match("aaaba")
        assert repeat("foo", 2).compile().match("foofoobar")
