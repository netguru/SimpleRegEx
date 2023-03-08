from copy import copy

from SimpleRegEx.models import RegEx
from SimpleRegEx.models import ensure_regex


def noneOrMany(what: RegEx):
    return ensure_regex(what) + "*"


def oneOrMore(what: RegEx):
    return ensure_regex(what) + "+"


def maybe(what: RegEx):
    return ensure_regex(what) + "?"


def group(what: RegEx, name=None):
    what = copy(ensure_regex(what))
    prefix = f"(?P<{name}>" if name else "("
    what._patterns = [prefix, *what._patterns, ")"]
    return what
    what = copy(ensure_regex(what))
    what._patterns.insert(0, "(")
    what._patterns.append(")")
    if name:
        what._patterns.insert(1, f"?P<{name}>")
    return what


def anyOfChar(items: str):
    return RegEx("[" + items + "]")
