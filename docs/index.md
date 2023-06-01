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

Provided pattern can occur many times or not at all.<br />
Here's an example of how you can use the `none_or_many` function:

```
from simpleregex.func import none_or_many

# Match zero or more occurrences of the string "abc"
pattern = none_or_many("abc")

# Compile the pattern and search for matches in a string
matches = pattern.compile().findall("abcabcabc")

# Print the matches
print(matches)  # Output: ['abc', 'abc', 'abc']
```

In this example, we create a regular expression that matches zero or more occurrences of the letter "a" using
the `none_or_many` function. We then compile the regular expression and search for a match in the string
"aaabbb". We print the matched substring using the print function, which outputs the string "aaa" to the console.

### `one_or_more(what: RegEx) -> RegEx`

Provided pattern can occur at least once.<br />
Here's an example of how you can use the `one_or_more` function:

```
from simpleregex.func import one_or_more

# Create a regular expression that matches one or more occurrences of "a"
pattern = one_or_more("a")

# Compile the regular expression and search for a match in a string
match = pattern.compile().search("aaabbb").group(0)

# Print the matched substring
print(match)  # Output: "aaa"
```

In this example, we use the `one_or_more` function to create a regular expression that matches one or
more occurrences of the letter "a". We then compile the regular expression and search for a match in
the string "aaabbb". The resulting match object contains a single group that matches the first three
"a" characters in the string. We print the matched substring using the print function, which outputs
the string "aaa" to the console.


### `none_or_one(what: RegEx) -> RegEx`

Provided pattern can occur once (but not more) or not at all.<br />
Here's an example of how you can use the `none_or_one` function:

```
from simpleregex.func import none_or_one

# Create a regular expression pattern for matching zero or one occurrences of 'a'
pattern = none_or_one("a")

# Search for the pattern in the input string 'aaabbb'
match = pattern.compile().search("aaabbb").group()

# Print the matched substring
print(match)  # Output: 'a'
```

In this example, we use the `none_or_one` function to create a regular expression that matches zero or one
occurrences of the letter "a". We then compile the regular expression and search for a match in the string "aaabbb".
The resulting match object contains a single group that matches the first "a" character in the string. We print
the matched substring using the print function, which outputs the string "a" to the console.

### `any_of_characters(regex_list: List[str]) -> RegEx`

Provided string is returned as a pattern of characters that can occur.<br />
Here's an example of how you can use the `any_of_characters` together with `regex_range` function:


```
from simpleregex.func import any_of_characters, regex_range

# Create a regular expression pattern for matching any one character from the range 'a' to 'z', digits 0 to 9, and the hyphen '-'
pattern = any_of_characters([regex_range('a', 'z'), regex_range(0, 9), '-']).compile()

# Search for the pattern in the input string 'ZzAbaaabbbaaa'
match = pattern.search('ZzAbaaabbbaaa').group()

# Print the matched substring
print(match)  # Output: 'z'
```

In this code snippet, we import the `any_of_characters` and `regex_range` functions from `simpleregex.func`.
We create a pattern that matches any character from the range 'a' to 'z', digits 0 to 9, and the hyphen '-'.
The pattern is compiled and then searched within the input string 'ZzAbaaabbbaaa'.
The matched substring, 'z', is printed.

### `regex_range(min: str, max: str) -> RegEx`

Range between two characters, for examle `regex_range('a', 'z')` will provide pattern: `[a-z]`<br />
Here's an example of how you can use the `regex_range` function:

```
from simpleregex.func import regex_range

# Create a regular expression pattern for matching any one character from the range '1' to '5'
pattern = regex_range(1, 5).compile()

# Search for the pattern in the input string '249'
match = pattern.search('249').group()

# Print the matched substring
print(match)  # Output: '2'
```

In this example, we import the `regex_range` function from the simpleregex.func module to create a regular
expression pattern that matches any one character from the range '1' to '5'. We compile the pattern into a
regular expression object and search for a match within the input string '249'. The resulting match object
contains a single group that corresponds to the matched character '2'. We retrieve the matched substring by
calling the group method on the match object. Finally, we print the matched substring, which is '2'.

### `group(what: RegEx, name=None, non_capturing=False) -> RegEx`

Groups provided pattern `what`.

- `name` - optional, name of the group
- `non_capturing` - if True, then not include this group when returning groups

Here's an example of how you can use the `group` function:
```
from simpleregex.func import group

# Create a regular expression pattern with a named capturing group
regex = group("foo", "bar").compile()

# Search for the pattern in the input string
match = regex.search("onefooone").groupdict()

# Access the captured group by name and print its value
print(match["bar"])  # Output: "foo"
```

In this example, we create a regular expression pattern using the group function with the pattern "foo" and
the name "bar" for the capturing group. The compile method is called on the pattern to compile it. Next, we
search for the pattern in the input string "onefooone" using the search method. The `groupdict` method is used
to retrieve the captured groups as a dictionary. We can access the value of the captured group named "bar"
by indexing the match dictionary with the key "bar". Finally, we print the value of the captured group,
which in this case is "foo".

### `look_ahead(what: RegEx, negative=False) -> RegEx`

- `negative` - If false an positive lookahead is generated. If True an negative lookahead is generated.
Assert if the certain pattern exists (or not) without actually matching it.
Use after the pattern that you want to match.

Here's an example of how you can use the `look_ahead` function:
```
# Import the necessary function
from simpleregex.func import look_ahead, RegEx

# Create a regular expression pattern with a negative lookahead
regex = (RegEx("Lorem ") + look_ahead("Ipsum", negative=True)).compile()

# You can print the pattern
print(regex.pattern)  # Output: "Lorem (?!Ipsum)"

# Use the pattern to match against the input string
re_match = regex.match("Lorem Ipsum")

# Assert that no match is found
assert re_match is None
```

We create a regular expression pattern by concatenating the string "Lorem " with a negative lookahead generated
by the `look_ahead` function. The negative parameter is set to True to create a negative lookahead. We compile the
pattern using the compile method and then we use the compiled pattern to match against the input string "Lorem Ipsum"
using the match method. We assert that no match is found by checking if the re_match object is None.

### `look_behind(what: RegEx, negative=False) -> RegEx`

- `negative` - If false an positive lookabehind is generated. If True an negative lookabehind is generated.
Assert if the certain pattern exists (or not) without actually matching it.
Use before the pattern that you want to match.

Here's an example of how you can use the `look_behind` function:
```
# Import the necessary function
from simpleregex.func import look_behind, RegEx

# Create a regular expression pattern with a positive lookbehind
regex = (look_behind("Lorem ") + RegEx("Ipsum")).compile()

# You can print the pattern
print(regex.pattern)  # Output: "(?<=Lorem )Ipsum"

# Search for the pattern in the input string
re_match = regex.search("Lorem Ipsum")

# Print the matched substring
print(re_match[0])  # Output: "Ipsum"
```
In this example, we create a regular expression pattern by concatenating a positive lookbehind generated by the
`look_behind` function with the pattern "Ipsum". The negative parameter is set to False to create a positive lookbehind.
We compile the pattern using the compile we use the compiled pattern to search for matches in the input string
"Lorem Ipsum" using the search method. Finally, we print the value of the matched substring,
which in this case is "Ipsum".

### `times(what: RegEx, min: int, max: int = None) -> RegEx`

Repeat a pattern between {min} and {max} times.</br>
Here's an example of how you can use the `times` function:
```
# Import the necessary function
from simpleregex.func import times, RegEx

# Create a regular expression pattern with repeated occurrences
regex1 = times("a", 1, 2).compile()
regex2 = times("a", 2, 3).compile()
regex3 = times("a", 3, 4).compile()

# Check if the pattern matches the input string
match1 = regex1.match("aa")
match2 = regex2.match("aa")
match3 = regex3.match("aa")

# Check if matches are found
if match1 is not None:
    print("Match found for regex1")

if match2 is not None:
    print("Match found for regex2")

if match3 is None:
    print("No match found for regex3")
```

In this example, we create three regular expression patterns using the `times` function to repeat the pattern "a"
a certain number of times. The min and max parameters are set to define the minimum and maximum repetition counts.
We compile the patterns using the compile method. Then, we use the match method to check if each pattern
matches the input string "aa". Finally, we check the match result which for match3 function is 'None', which
means that no match was found.

### `repeat(what: RegEx, count: int) -> RegEx`

Repeat a pattern {count} times.</br>
Here's an example of how you can use the `repeat` function:

```
from simpleregex.func import repeat

# Repeat the pattern 'a' 2 times
pattern = repeat("a", 2).compile()

# Check if the pattern matches the input string 'aaba'
match_1 = pattern.match("aaba")
assert match_1  # The pattern matches the input string

# Check if the pattern matches the input string 'aaaba'
match_2 = pattern.match("aaaba")
assert match_2  # The pattern matches the input string
```

In this example, we create a regular expression pattern using the `repeat` function to repeat the pattern "a".
The repeat function takes two parameters: `what`, which represents the pattern to be repeated, and `count`,
which specifies the number of times the pattern should be repeated. We create a pattern by calling
repeat("a", 2).compile(), which repeats the character 'a' two times. We then use the match method of the
compiled pattern to check if the pattern matches the input strings 'aaba' and 'aaaba'. The first match,
match_1, is expected to return Match object since the pattern 'aa' is present in 'aaba'. Similarly, the
second match, match_2, is also expected to return Match object since the pattern 'aaa' is present in 'aaaba'.

### `negate(what: RegEx) -> RegEx`

Negate either exact characters or ranges.
To Negate whole expressions use negative lookarounds.

```
from simpleregex.func import negate

# Create a regular expression pattern by negating the range "a" to "z"
pattern = negate(regex_range("a", "z")).compile()

# Search for the pattern in the input string "fooBAR"
re_match = pattern.search("fooBAR")

# Print the matched substring
print(re_match[0])  # Output: "B"
```

In this example, we create a regular expression pattern by negating the range "a" to "z" using the `negate` function.
Next, we search for the pattern in the input string "fooBAR" using the search method. The search method returns
a match object that contains information about the matched substring. Finally, we print the matched substring
using print(`re_match[0]`). In this case, the output will be "B", which represents the first character in the input
string that matches the negated pattern.

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
