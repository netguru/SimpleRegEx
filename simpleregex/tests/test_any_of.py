# -*- coding: utf-8 -*-
from simpleregex.func import any_of
from simpleregex.func import group
from simpleregex.models import RegEx


class TestAnyOf:
    def test_any_of_multiple_groups(self):
        regex = any_of([group("Lorem"), group("Ipsum"), "Donor"]).compile()

        assert regex.pattern == "((Lorem)|(Ipsum)|Donor)"

        match = regex.match("Lorem Ipsum Donor")
        assert match is not None
        assert match[0] == "Lorem"

    def test_any_of_multiple_groups_no_result(self):
        regex = any_of(["Sit", "Amet", "Consectetur"]).compile()

        assert regex.pattern == "(Sit|Amet|Consectetur)"

        match = regex.match("Lorem ipsum dolor")
        assert match is None

    def test_any_of_multiple_groups_after_string(self):
        regex = (RegEx("Lorem ") + any_of(["Ipsum", "Donor"])).compile()

        assert regex.pattern == "Lorem (Ipsum|Donor)"

        match = regex.match("Lorem ipsum dolor")
        assert match is None
