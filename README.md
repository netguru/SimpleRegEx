<div align="center">
  <h1>Simple RegEx</h1>
</div>

<div align="center">
    <img src="https://circleci.com/gh/netguru/SimpleRegEx.svg?style=svg" alt="CircleCI status"></img>
</div>

<div align="center">
  <br/>
<em>Brought with</em>&nbsp;❤️&nbsp;<em>by</em>&nbsp;
<a href="https://www.netguru.com">
<img align="center" alt="Netguru logo" src='https://raw.githubusercontent.com/netguru/SimpleRegEx/main/docs/readme_netguru_logo.png' width='30'/></a>
</div>

# Introduction

<p align="center">
  Readability counts. Even in regex.
</p>

<div align="center">

[Documentation](https://github.com/netguru/SimpleRegEx/blob/main/docs/index.md) &nbsp;|&nbsp;
[About](#about) &nbsp;|&nbsp;
[Installation](#installation) &nbsp;|&nbsp;
[Contributing](https://github.com/netguru/SimpleRegEx/blob/main/docs/CONTRIBUTING.md) &nbsp;

</div>

# <a name="about"></a>About

This tool is a wrapper for RegEx in python (`import re`), which introduces pattern
functions in place of unreadable text patterns.

This tool is inspired by the [Magic Regex](https://github.com/danielroe/magic-regexp) tool.

# In Use

Usage example can be found
in [unit tests](https://github.com/netguru/SimpleRegEx/blob/main/simpleregex/tests/test_email.py).

# <a name="installation"></a>Installation

```
pip install simpleregex
```

# Release

To bump a package version use poetry. Examples can be found
in [poetry docs](https://python-poetry.org/docs/cli/#version).

The release process is automated on circle ci.
Merge to main branch will deploy automated release to test.pypi.org.
To release the new package version to pypi.org create a tag for selected version `v\d+\.\d+\.\d+`.

# Support

Supported python versions:

- 3.11
- 3.10
- 3.9
- 3.8
