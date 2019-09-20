# Cookiecutter Template – Python Package 🐍📦

This project contains a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template that allows us to easily build out fully intialized Python packages that are ready for publishing right out of the box. We also add in a whole bunch of tooling to benefit the development experience and promote project sustainability.

## Usage

First make sure that you have [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) installed:

```console
$ pip install --user cookiecutter
```

Then request and execute the template using:

```console
$ cookiecutter gh:modist-io/cookiecutter-python-package
```

This will prompt you to enter a couple fields to understand how to generate the project.
This template will:

1. Setup the full package structure and configuration files as well as create a couple starting `__init__.py` files for the package and the corresponding tests
2. Initialize a new git repository and point the origin to the correct GitHub route
3. Build a local virtual environment with initial package testing and documentaion building dependencies
4. Install and initialize environments for necessary pre-commit hooks
5. Add all generated files to an initial commit and prompt the user to enter a valid commit message

### Installing Dependencies

Because we are trying to build a packaged project, we need to install specific packages in different ways (since Python's package management structure sucks).
By following these guidelines, we can ensure that our project doesn't get too bloated and can be easily installable everywhere without having to re-declare dependencies in multiple files.

If you are installing a **development** dependency, utilize `pipenv`.

```console
$ pipenv install <DEPENDENCY NAME> --dev
```

If you are installing a **required** dependency, add the dependecy to the `install_requires` section in `setup.cfg`.

```console
... <snipped setup.cfg> ...

[options]
zip_safe = true
python_requires = >=3.6
setup_requires = setuptools>=36.2.2
install_requires =
    <DEPENDENCY NAME>
```

If you are installing an **extra dependency** (such as those required for testing or documentation building), add the dependency to the `options.extras_require` section in `setup.cfg`

```console
... <snipped setup.cfg> ...

[options.extras_require]
test =
    isort
    flake8
    pytest
    pytest-flake8
    pytest-sugar
    pytest-xdist
    pytest-cov
    hypothesis
    codacy-coverage
    coverage
    check-manifest
docs =
    sphinx
```

### Project Tasks

We have written and included a couple invoke tasks that are used as an abstraction to do many project releated tasks.
You **must** run the invoke scripts using the `pipenv run invoke <TASK NAME>` or `pipenv run inv <TASK NAME>` syntax.
Most of these tasks are pretty self-explanitory.

> Be cautious of modifying these tasks to a great extent. Other files and scripts (such as pre-commit hooks) depend on these tasks executing a certain way.

```console
$ pipenv run invoke -l
Available tasks:

  build                  Build the project.
  clean                  Clean the project.
  profile                Run and profile a given Python script.
  publish                Publish the project.
  test                   Test the project.
  docs.build             Build docs.
  docs.build-news        Build towncrier newsfragments.
  docs.clean             Clean built docs.
  docs.view              Build and view docs.
  package.build          Build pacakge source files.
  package.check          Check built package is valid.
  package.clean          Clean previously built package artifacts.
  package.format         Auto format package source files.
  package.licenses       List dependency licenses.
  package.requirements   Generate requirements.txt from Pipfile.lock.
  package.stub           Generate typing stubs for the package.
  package.test           Run package tests.
  package.typecheck      Run type checking with generated package stubs.
  package.version        Specify a new version for the package.
```

## Caveats

A couple caveats do exist with the resulting generated package.
Please take note of these to avoid initial confusion:

- This template is **very much** aimed towards build packages branded and licensed by the Modist team.
    So if you want to utilize the same tooling we do for our packages, you might want to fork this repository and play with some of the defaults in `cookiecutter.json`.
- In order for Github CI (actions) to properly work, several [Github secrets](https://help.github.com/en/articles/virtual-environments-for-github-actions#creating-and-using-secrets-encrypted-variables) need to be added to the Github repository:
    - `CODECOV_TOKEN` - The token used for reporting coverage to [Codecov](https://codecov.io), you can find the relevant token at `https://codecov.io/gh/<GITHUB-USERNAME>/<GITHUB-REPOSITORY-NAME>/settings`
    - `CODACY_PROJECT_TOKEN` - The coverage token for the [Codacy](codacy.com) app, you can find the relevant token at `https://app.codacy.com/manual/<GITHUB-USERNAME>/<GITHUB-REPOSITORY-NAME>/settings/coverage`
- A `requirements.txt` file is required for Read The Docs (`.readthedocs.yml`), however one is not generated or supplied by default.
    As project dependencies change, this file will need to be **manully** regenerated.
    We have provided a quick task that basically will generate this file for you:

    ```console
    $ pipenv run invoke package.requirements
    [package.requirements] ... generating requirements.txt from Pipfile.lock
    ```
