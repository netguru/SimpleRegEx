<div align="center">
  <h1>Simple RegEx</h1>
</div>

<div align="center">
    <image src="https://circleci.com/gh/netguru/SimpleRegEx.svg?style=svg"/>
</div>

<div align="center">
  <br/><em>Brought with</em> &nbsp;❤️ <em>by</em> &nbsp; <a href="https://www.netguru.com"><img align="center" alt="Netguru logo" src='./docs/readme_netguru_logo.png' width='30'/></a>
</div>

# Introduction

<p align="center">
  Readability counts. Even in regex.
</p>

<div align="center">
  <a href="./docs/index.md">Documentation</a> &nbsp;|&nbsp; <a href="#About">About</a> &nbsp;|&nbsp; <a href="#Installation">Installation</a> &nbsp;|&nbsp; <a href="./docs/CONTRIBUTING.md">Contributing</a> &nbsp;
</div>

# About

This tool is a wrapper for RegEx in python (`import re`), which introduces pattern
functions in place of unreadable text patterns.

This tool is inspired by the [Magic Regex](https://github.com/danielroe/magic-regexp) tool.

# In Use

```python
pattern = (
    RegEx("\\.")
    + SPACE
    + group(
        noneOrMany(any_of_characters([WORD, SPACE]))
        + "Przem"
        + any_of(["ysław", "ek", "ka"])
        + SPACE
        + "Mazur"
        + any_of(["ek", "ka"])
        + noneOrMany(any_of_characters([WORD, SPACE]))
    )
    + RegEx("\\.")
)
```

# Installation

```
pip install simpleregex
```

# Support

 Supported python versions:
 - 3.11
 - 3.10
 - 3.9
 - 3.8
