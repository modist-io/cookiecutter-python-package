.. raw:: html

   <h1 align="center" style="font-size: 64px;">{{ cookiecutter.project_title }}</h1>
   <p align="center" style="margin: 0px;">
      <a href="https://pypi.org/project/{{ cookiecutter.project_slug }}/" target="_blank"><img alt="Supported Versions" src="https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg"></a>
      <a href="https://github.com/ambv/black" target="_blank"><img alt="Code Style: Black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
   </p>


{{ cookiecutter.project_description }}


**To get started using this package, please see the** :ref:`getting-started` **page!**

User Documentation
------------------

.. toctree::
   :maxdepth: 2

   getting-started
   contributing
   changelog


Project Reference
-----------------

.. toctree::
   :maxdepth: 2

   {{ cookiecutter.package_name }}