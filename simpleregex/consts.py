# -*- coding: utf-8 -*-
from simpleregex.models import RegEx

ANY_CHARACTER = RegEx(".")
BEGINING = RegEx("^")
END = RegEx("$")
WORD = RegEx(r"\w")
NEW_LINE = RegEx(r"\n")
ALNUM = RegEx("[:alnum:]")
ALPHA = RegEx("[:alpha:]")
ASCII = RegEx("[:ascii:]")
BLANK = RegEx("[:blank:]")
CNTRL = RegEx("[:cntrl:]")
DIGIT = RegEx("[:digit:]")
GRAPH = RegEx("[:graph:]")
LOWER = RegEx("[:lower:]")
PRINT = RegEx("[:print:]")
PUNCT = RegEx("[:punct:]")
SPACE = RegEx("\\s")
UPPER = RegEx("[:upper:]")
XDIGIT = RegEx("[:xdigit:]")