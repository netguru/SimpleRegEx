from SimpleRegEx.func import anyOfChar


class TestanyOfChar:
    def test_none(self):
        assert not anyOfChar("a").compile().match("bbb")

    def test_one(self):
        match = anyOfChar("a").compile().search("abbb")
        assert match[0] == "a"

    def test_many(self):
        match = anyOfChar("ab").compile().search("ZzAbaaabbbaaa")
        assert match[0] == "b"
