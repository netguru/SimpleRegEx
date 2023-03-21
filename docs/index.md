# SimpleRegex

## Basics

Every pattern created by the SimpleRegex returns an RegEx object.

```
from simpleregex.models import RegEx
```

This object can be added to another string and will create another RegEx object.

```
pattern = RegEx("^") + ".*$"
```

Also, every function is supporting RegEx object or strings.

```
pattern = none_or_many('string')
```

## RegEx Reference `simpleregex.models`

### `RegEx.compile() -> re.Pattern`

Returns compiled python re object.

### `RegEx.pattern -> string`

Returns pattern

## Functions Reference `simpleregex.func`

### `none_or_many(what: RegEx) -> RegEx`

Provided pattern can occure many times or not at all.

### `one_or_more(what: RegEx) -> RegEx`

Provided pattern can occure at lest once

### `none_or_one(what: RegEx) -> RegEx`

Provided pattern can occure once (but not more) or not at all.

### `any_of_char(items: str) -> RegEx`

Provided string is returned as pattern of characters that can be occure.

### `regex_range(min: str, max: str) -> RegEx`

Range between two characters, for examle `regex_range('a', 'z')` will provide
pattern: `[a-z]`

### `group(what: RegEx, name=None, non_capturing=False) -> RegEx`

Groups provided pattern `what`.

- `name` - optional, name of the group
- `non_capturing` - if True, then not include this group when returing groups

### `look_ahead(what: RegEx, negative=False) -> RegEx`

- `negative` - If false an positive lookahead is generated. If True an negative lookahead is generated.
Assert if the certain pattern exists (or not) without actually matching it.
Use after the pattern that you want to match.

### `look_behind(what: RegEx, negative=False) -> RegEx`

- `negative` - If false an positive lookabehind is generated. If True an negative lookabehind is generated.
Assert if the certain pattern exists (or not) without actually matching it.
Use before the pattern that you want to match.

### `any_of_characters(regex_list: List[str]) -> RegEx`



### `times(what: RegEx, min: int, max: int = None) -> RegEx`

Repeate a pattern between {min} and {max} times.

### `repeat(what: RegEx, count: int) -> RegEx`

Repeate a pattern {count} times.

### `negate(what: RegEx) -> RegEx`

Negate either exact characters or ranges.
To Negate whole expressions use negative lookarounds.

## Consts Reference `simpleregex.consts`

- ANY_CHARACTER - `.`
- BEGINING - `^` - beggining of a pattern/string
- END - `$` - end of a pattern/string
- NEW_LINE - `\n`
- WORD - `\w` - Word characters (letters, numbers and underscores)
- ALNUM - `:alnum:` - Alphanumeric characters
- ALPHA - `:alpha:` - Alphabetic characters
- ASCII - `:ascii:` - ASCII characters
- BLANK - `:blank:` - Space and tab
- CNTRL - `:cntrl:` - Control characters
- DIGIT - `:digit:` - Digits
- GRAPH - `:graph:` - Visible characters (anything except spaces and control characters)
- LOWER - `:lower:` - Lowercase letters
- PRINT - `:print:` - Visible characters and spaces (anything except control characters)
- PUNCT - `:punct:` - Punctuation (and symbols).
- SPACE - `:space:` - All whitespace characters, including line breaks
- UPPER - `:upper:` - Uppercase letters
- XDIGIT - `:xdigit:` - Hexadecimal digits
