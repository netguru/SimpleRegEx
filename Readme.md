# SimpleRegEx

Readability counts. Even in regex.

This tool is a wrapper for RegEx in python (`import re`), which introduces pattern
functions in place of unreadable text patterns.

[Documentation](./docs/index.md)

# Support

 Supported python versions:
 - 3.11
 - 3.10
 - 3.9
 - 3.8

# Development
pre-commit hook is added and configured for this project. Before commiting your first changes please run:
```bash
pre-commit install
```


## Local setup
This project uses poetry as a package management tool, make sure you have it installed and added to path. Once that's done run:
```bash
poetry install
```


## Running tests
### Make sure you have tox installed
MacOS
```bash
brew install tox
```
Linux
```bash
apt-get install tox
```
#### Run tests for all supported python versions
```bash
tox
```
#### Run tests for a selected python version
```bash
tox -e py310
```
