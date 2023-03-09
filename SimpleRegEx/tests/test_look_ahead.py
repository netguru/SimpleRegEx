from SimpleRegEx.models import RegEx
from SimpleRegEx.func import look_ahead


class TestLookAhead:
    def test_positive_lookahead(self):
        regex = (RegEx("Lorem ") + look_ahead("Ipsum")).compile()

        assert regex.pattern == "Lorem (?=Ipsum)"

        match = regex.match("Lorem Ipsum")
        assert match is not None
        assert match[0] == "Lorem "

    def test_positive_lookahead_not_found(self):
        regex = (RegEx("Lorem ") + look_ahead("Ipsum")).compile()

        assert regex.pattern == "Lorem (?=Ipsum)"

        match = regex.match("Lorem Amet")
        assert match is None

    def test_negative_lookahead(self):
        regex = (
            RegEx("Lorem ") + look_ahead("Ipsum", negative=True)
        ).compile()

        assert regex.pattern == "Lorem (?!Ipsum)"

        match = regex.match("Lorem Amet")
        assert match is not None
        assert match[0] == "Lorem "

    def test_negative_lookahead_not_found(self):
        regex = (
            RegEx("Lorem ") + look_ahead("Ipsum", negative=True)
        ).compile()

        assert regex.pattern == "Lorem (?!Ipsum)"

        match = regex.match("Lorem Ipsum")
        assert match is None