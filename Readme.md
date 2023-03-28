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

Usege example can be found in [unit tests](https://github.com/netguru/SimpleRegEx/blob/main/simpleregex/tests/test_email.py).

# Installation

```
pip install simpleregex
```

# Release
To bump a package version use poetry. Examples can be found in [potry docs](https://python-poetry.org/docs/cli/#version).

The release process is automated on circle ci.
Merge to main branch will deploy automated release to test.pypi.org.
To release the new package version to pypi.org create a tag for selected version `v\d+\.\d+\.\d+`.

# Support

 Supported python versions:
 - 3.11
 - 3.10
 - 3.9
 - 3.8
