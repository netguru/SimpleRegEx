# -*- coding: utf-8 -*-
from simpleregex.func import group


class TestGroup:
    def test_when_found(self):
        assert group("abc").compile().search("oneabcone")[0] == "abc"

    def test_when_not_found(self):
        assert not group("abc").compile().search("oneacone")

    def test_when_name_provided(self):
        regex = group("abc", "meme").compile()
        result = regex.search("oneabcone").groupdict()
        assert result["meme"] == "abc"

    def test_none_capturing_group(self):
        regex = (
            group("abc", "not_captured", non_capturing=True)
            + group("one", "captured")
        ).compile()

        assert regex.pattern == "(?:abc)(?P<captured>one)"

        result = regex.search("oneabcone").groupdict()
        assert "not_captured" not in result
        assert "captured" in result
