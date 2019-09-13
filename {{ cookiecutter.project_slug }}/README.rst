{{ cookiecutter.project_title }}
{{ cookiecutter.project_title|count * "=" }}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg
   :target: https://pypi.org/project/{{ cookiecutter.project_slug }}/
   :alt: Supported Versions

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Test%20Package/badge.svg
    :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions
    :alt: Test Status

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
   :target: https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code Style: Black
