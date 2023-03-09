from simpleregex.func import or_


class TestOr:
    def test_when_match(self):
        assert or_("a", "b").compile().match("a")

    def test_when_not_match(self):
        assert not or_("a", "b").compile().match("c")
