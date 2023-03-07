from SimpleRegEx.func import maybe


class TestMaybe:
    def test_none(self):
        assert maybe("a").compile().match("bbb")

    def test_one(self):
        match = maybe("a").compile().search("abbb")
        assert match[0] == "a"

    def test_many(self):
        match = maybe("a").compile().search("aaabbb")
        assert match[0] == "a"
