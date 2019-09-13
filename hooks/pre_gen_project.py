# -*- encoding: utf-8 -*-
# Copyright (c) 2019 Stephen Bunn <stephen@bunn.io>
# ISC License <https://opensource.org/licenses/isc>

import shutil


if not shutil.which("git"):
    raise OSError(
        "generating this project requires git <https://git-scm.com/>, "
        "but we can't find it on your system"
    )

if not shutil.which("pipenv"):
    raise OSError(
        "initializing the virtual environment requires pipenv "
        "<https://docs.pipenv.org/en/latest/>, but we can't find it on your system"
    )
