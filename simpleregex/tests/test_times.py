# -*- coding: utf-8 -*-
from simpleregex.func import times


class TestTimes:
    def test_when_provided_only_min(self):
        assert times("a", 1).compile().match("aa")
        assert times("a", 2).compile().match("aa")
        assert not times("a", 3).compile().match("aa")

    def test_when_provided_range(self):
        assert times("a", 1, 2).compile().match("aa")
        assert times("a", 2, 3).compile().match("aa")
        assert not times("a", 3, 4).compile().match("aa")
