# -*- coding: utf-8 -*-
from simpleregex.func import regex_range


class TestGroup:
    def test_when_found(self):
        regex = regex_range(1, 5).compile()

        assert regex.pattern == "[1-5]"

        assert regex.search("249")[0] == "2"

    def test_when_not_found(self):
        regex = regex_range(0, 1).compile()

        assert regex.pattern == "[0-1]"

        assert regex.search("249") is None
