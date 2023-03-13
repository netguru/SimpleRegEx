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

## RegEx Reference

### RegEx.compile() -> re.Pattern

Returns compiled python re object.

### RegEx.pattern -> string

Returns pattern

## Functions Reference

### none\_or\_many(what: RegEx) -> RegEx

## Consts Reference
