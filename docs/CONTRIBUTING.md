# Contributing

## Running/Development
This project uses poetry as a package management tool, make sure you have it installed and added to path. Once that's done run:
```sh
poetry install
```

## Running Tests
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

## Creating new Pull Request
* remember to add appropriate title, ticket, description
* adding code snippet is very beneficial but it's not mandatory
* additionally please remember to add appropriate Pull Request title from following:
  * `short description` - for normal feature branches
* remember one pull request should always address one issue or feature

## Code structure
```
simpleregex/
├──code
docs/
├──documentation
```

## Code Style
* Linting rules are defined in `.pre-commit-config.yaml` and enforced by pre-commit hook. Make sure you have it installed before commiting.
  ```sh
  pre-commit install
  ```

* Name branch according to your ticket following this pattern: (feature/bugfix)/BN-XXX-short_description
