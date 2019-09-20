# -*- encoding: utf-8 -*-
# Copyright (c) {{ cookiecutter.year }} {{ cookiecutter.author }} <{{ cookiecutter.email }}>
# {{ cookiecutter.licenses[cookiecutter.package_license].name }} <{{ cookiecutter.licenses[cookiecutter.package_license].url }}>

"""This moudle exposes some initial package building sanity checks."""


def test_version_importable():
    """Basic sanity check to ensure we can discover the package name and version."""

    from {{ cookiecutter.package_name }} import __version__

    assert isinstance(__version__.__name__, str)
    assert isinstance(__version__.__version__, str)
