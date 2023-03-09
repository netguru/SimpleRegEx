from copy import copy

from SimpleRegEx.models import RegEx
from SimpleRegEx.models import ensure_regex


def noneOrMany(what: RegEx):
    return ensure_regex(what) + "*"


def oneOrMore(what: RegEx):
    return ensure_regex(what) + "+"


def maybe(what: RegEx):
    return ensure_regex(what) + "?"


def anyOfChar(items: str):
    return RegEx("[" + items + "]")


def _wrap_regex(what: RegEx, prefix: str, suffix: str):
    what = copy(ensure_regex(what))
    what._patterns = [prefix, *what._patterns, suffix]
    return what


def group(what: RegEx, name=None):
    return _wrap_regex(what, f"(?P<{name}>" if name else "(", ")")


def look_ahead(what: RegEx, negative=False):
    return _wrap_regex(what, f"(?!" if negative else "(?=", ")")


def look_behind(what: RegEx, negative=False):
    return _wrap_regex(what, f"(?<!" if negative else "(?<=", ")")
