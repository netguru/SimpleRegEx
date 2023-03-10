# -*- coding: utf-8 -*-
from typing import List
from typing import Union

from simpleregex.models import ensure_regex
from simpleregex.models import RegEx


def none_or_many(what: RegEx):
    return ensure_regex(what) + "*"


def one_or_more(what: RegEx):
    return ensure_regex(what) + "+"


def maybe(what: RegEx):
    return ensure_regex(what) + "?"


def any_of_char(items: str):
    return RegEx("[" + items + "]")


def regex_range(min: str, max: str):
    return RegEx(["[", str(min), "-", str(max), "]"])


def _wrap_regex(what: RegEx, prefix: str, suffix: str):
    what = ensure_regex(what)
    what._patterns = [*list(prefix), *what._patterns, *list(suffix)]
    return what


def group(what: RegEx, name=None, non_capturing=False):
    if non_capturing is True:
        return _wrap_regex(what, "(?:", ")")
    return _wrap_regex(what, f"(?P<{name}>" if name else "(", ")")


def look_ahead(what: RegEx, negative=False):
    return _wrap_regex(what, f"(?!" if negative else "(?=", ")")


def look_behind(what: RegEx, negative=False):
    return _wrap_regex(what, f"(?<!" if negative else "(?<=", ")")


def or_(left: RegEx, right: RegEx):
    left = ensure_regex(left)
    right = ensure_regex(right)
    return left + "|" + right


def any_of(regex_list: List[Union[str, RegEx]]):
    what = RegEx("(")
    for index, item in enumerate(regex_list):
        item = ensure_regex(item)
        if index != 0:
            what += "|"
        what += item
    return what + ")"


def any_of_characters(regex_list: List[str]):
    what = RegEx("[")
    for item in regex_list:
        what += ensure_regex(item)
    return what + "]"


def times(what: RegEx, min: int, max: int = None):
    """
    Repeate a pattern between {min} and {max} times.
    """
    what = ensure_regex(what)
    return what + (f"{{{min},}}" if max is None else f"{{{min},{max}}}")


def repeat(what: RegEx, count: int):
    """
    Repeate a pattern {count} times.
    """
    return ensure_regex(what) + f"{{{count}}}"


def negate(what: RegEx):
    """
    Negate either exact characters or ranges.
    To Negate whole expressions use negative lookarounds.
    """
    what = ensure_regex(what)
    if what._patterns[0] == "[":
        what._patterns.insert(1, "^")
        return what
    else:
        return _wrap_regex(what, f"[^", "]")
