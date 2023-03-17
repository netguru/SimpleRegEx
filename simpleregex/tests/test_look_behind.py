# -*- coding: utf-8 -*-
from simpleregex.func import look_behind
from simpleregex.models import RegEx


class TestLookBehind:
    def test_positive_lookbehind(self):
        regex = (look_behind("Lorem ") + RegEx("Ipsum")).compile()

        assert regex.pattern == "(?<=Lorem )Ipsum"

        re_match = regex.search("Lorem Ipsum")
        assert re_match is not None
        assert re_match[0] == "Ipsum"

    def test_positive_lookbehind_not_found(self):
        regex = (look_behind("Lorem ") + RegEx("Ipsum")).compile()

        assert regex.pattern == "(?<=Lorem )Ipsum"

        re_match = regex.search("Amet Ipsum")
        assert re_match is None

    def test_negative_lookbehind(self):
        regex = (
            look_behind("Lorem ", negative=True) + RegEx("Ipsum")
        ).compile()

        assert regex.pattern == "(?<!Lorem )Ipsum"

        re_match = regex.search("Amet Ipsum")
        assert re_match is not None
        assert re_match[0] == "Ipsum"

    def test_negative_lookbehind_not_found(self):
        regex = (
            look_behind("Lorem ", negative=True) + RegEx("Ipsum")
        ).compile()

        assert regex.pattern == "(?<!Lorem )Ipsum"

        re_match = regex.search("Lorem Ipsum")
        assert re_match is None
