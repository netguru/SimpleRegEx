from copy import deepcopy
from dataclasses import dataclass
from dataclasses import field
from re import compile


@dataclass
class RegEx:
    _patterns: list = field(default_factory=list)

    def compile(self, flags=0):
        return compile(self.pattern, flags)
        pattern = "".join(self._patterns)
        return compile(pattern, flags)

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
        return obj
    elif isinstance(obj, str):
        return RegEx(_patterns=[obj])
    else:
        raise TypeError()
