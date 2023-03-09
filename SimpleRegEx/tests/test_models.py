# -*- coding: utf-8 -*-
from pytest import raises

from SimpleRegEx.models import ensure_regex
from SimpleRegEx.models import RegEx


class TestRegex:
    def test_pattern(self):
        """
        .pattern should return pattern in plain string
        """
        regex = RegEx(["one", "two", "%^"])
        assert regex.pattern == "onetwo%^"

    def test_add(self):
        """
        adding two RegEx should return one merged RegEx.
        Both objects should not be changed.
        """
        left = RegEx(["a"])
        right = RegEx(["b"])
        assert (left + right).pattern == "ab"
        assert left.pattern == "a"
        assert right.pattern == "b"


class TestEnsureRegex:
    def test_when_regex(self):
        """
        When object is a RegEx, return it.
        """
        left = RegEx()
        assert id(ensure_regex(left)) == id(left)

    def test_when_str(self):
        """
        When object is a str, return RegEx object.
        """
        assert ensure_regex("something").pattern == "something"

    def test_when_other(self):
        """
        When object is of other types, raise TypeError
        """
        with raises(TypeError):
            ensure_regex(1)
