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
simpleregext/
├──code
docs/
├──documentation
```

## Code Style
* Make sure to install pre-commit hook
  ```sh
  pre-commit install
  ```

* Make sure you are using linter with linting rules defined in ESLint config (.eslintrc.js)
* Name branch according to your ticket following this pattern: RNS-XX-short_description
* Imports and exports inside `index.tsx` files eg. `screens/index.tsx`, `components/index.tsx` should be sorted alphabetically
* Style names should be ordered alphabetically
* Please use commit lint and follow commit naming convention (https://www.conventionalcommits.org/en/v1.0.0/)
