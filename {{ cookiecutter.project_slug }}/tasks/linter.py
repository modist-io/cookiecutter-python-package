# -*- encoding: utf-8 -*-
# Copyright (c) 2020 Modist Team <admin@modist.io>
# ISC License <https://opensource.org/licenses/isc>

"""Contains Invoke task functions for source checks and linters."""

import invoke

from .utils import report


@invoke.task
def flake8(ctx, verbose=False):
    """Run Flake8 tool against source."""

    report.info(ctx, "linter.flake8", "running Flake8 check")
    flake8_command = "flake8 src/* tests/*"
    if verbose:
        flake8_command += " --verbose"

    ctx.run(flake8_command)


@invoke.task
def black(ctx, verbose=False):
    """Run Black tool check against source."""

    report.info(ctx, "linter.black", "running Black check")
    black_command = "black --check src/* tests/*"
    if verbose:
        black_command += " --verbose"

    ctx.run(black_command)


@invoke.task
def isort(ctx, verbose=False):
    """Run ISort tool check against source."""

    report.info(ctx, "linter.isort", "running ISort check")
    isort_command = "isort --check-only src/**/*.py tests/**/*.py"
    if verbose:
        isort_command += " --verbose"

    ctx.run(isort_command)


@invoke.task
def mypy(ctx, verbose=False):
    """Run MyPy tool check against source."""

    report.info(ctx, "linter.mypy", "running MyPy check")
    mypy_command = "mypy src tests"
    if verbose:
        mypy_command += " --verbose"

    ctx.run(mypy_command)
