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

To bump a package version go to [setup.py](https://github.com/netguru/SimpleRegEx/blob/main/setup.py) and
change `version` variable.

Create new release on GitHub and tag it with the same version as in `setup.py`.

The release process to `testpypi` and `pypi` is manually triggered on CircleCi.
After successful merge to main and creation of new release tag, go to
[CircleCi](https://app.circleci.com/pipelines/github/netguru/SimpleRegEx?branch=main) and trigger new pipeline with
following boolean parameters:
- `pypi_publish: true` - this will push package to `pypi`
- `testpypi_publish: true` - this will push package to `testpypi`

# Support

Supported python versions:

- 3.11
- 3.10
- 3.9
- 3.8
