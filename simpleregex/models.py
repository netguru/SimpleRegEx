# -*- coding: utf-8 -*-
from copy import deepcopy
from dataclasses import dataclass
from dataclasses import field
from re import compile
from re import Pattern


@dataclass
class RegEx:
    _patterns: list = field(default_factory=list)

    def __post_init__(self):
        if isinstance(self._patterns, str):
            self._patterns = [self._patterns]

    def compile(self, flags=0) -> Pattern:
        return compile(self.pattern, flags)

    @property
    def pattern(self):
        return "".join(self._patterns)

    def __add__(self, right):
        left = deepcopy(self)
        if isinstance(right, str):
            left._patterns.append(right)
        else:
            left._patterns += right._patterns
        return left


def ensure_regex(obj):
    if isinstance(obj, RegEx):
        return deepcopy(obj)
    elif isinstance(obj, str):
        return RegEx(_patterns=[obj])
    else:
        raise TypeError(f"RegEx or string is required, got {type(obj)}")
