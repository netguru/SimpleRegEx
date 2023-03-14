# -*- coding: utf-8 -*-
from simpleregex.func import look_ahead
from simpleregex.models import RegEx


class TestLookAhead:
    def test_positive_lookahead(self):
        regex = (RegEx("Lorem ") + look_ahead("Ipsum")).compile()

        assert regex.pattern == "Lorem (?=Ipsum)"

        re_match = regex.match("Lorem Ipsum")
        assert re_match is not None
        assert re_match[0] == "Lorem "

    def test_positive_lookahead_not_found(self):
        regex = (RegEx("Lorem ") + look_ahead("Ipsum")).compile()

        assert regex.pattern == "Lorem (?=Ipsum)"

        re_match = regex.match("Lorem Amet")
        assert re_match is None

    def test_negative_lookahead(self):
        regex = (RegEx("Lorem ") + look_ahead("Ipsum", negative=True)).compile()

        assert regex.pattern == "Lorem (?!Ipsum)"

        re_match = regex.match("Lorem Amet")
        assert re_match is not None
        assert re_match[0] == "Lorem "

    def test_negative_lookahead_not_found(self):
        regex = (RegEx("Lorem ") + look_ahead("Ipsum", negative=True)).compile()

        assert regex.pattern == "Lorem (?!Ipsum)"

        re_match = regex.match("Lorem Ipsum")
        assert re_match is None
