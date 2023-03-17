# -*- coding: utf-8 -*-
from simpleregex.func import negate
from simpleregex.func import regex_range


class TestGroup:
    def test_when_found(self):
        regex = negate(regex_range("a", "z")).compile()

        assert regex.pattern == "[^a-z]"

        assert regex.search("loreM")[0] == "M"

    def test_when_not_found(self):
        regex = negate(regex_range("a", "z")).compile()

        assert regex.pattern == "[^a-z]"

        assert regex.search("lorem") is None

    def test_negate_string(self):
        regex = negate("L").compile()

        assert regex.pattern == "[^L]"

        assert regex.search("LoreM")[0] == "o"
