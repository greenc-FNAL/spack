# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPlatformdirs(PythonPackage):
    """A small Python module for determining appropriate
    platform-specific dirs, e.g. a "user data dir" """

    homepage = "https://github.com/platformdirs/platformdirs"
    pypi = "platformdirs/platformdirs-2.4.0.tar.gz"

    version('2.4.1', sha256='440633ddfebcc36264232365d7840a970e75e1018d15b4327d11f91909045fda')
    version("2.4.0", sha256="367a5e80b3d04d2428ffa76d33f124cf11e8fff2acdaa9b43d545f5c7d661ef2")
    version('2.3.0', sha256='15b056538719b1c94bdaccb29e5f81879c7f7f0f4a153f46086d155dffcd4f0f')

    depends_on("python@3.7:", when="@2.4.1:", type=("build", "run"))
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools@44:", type="build")
    depends_on("py-setuptools-scm@5:+toml", type="build")


    @when("^python@:3.6")
    @run_before("install")
    def handle_utf8_setup_cfg(self):
        """Sanitize setup.cfg to resolve issues with Python 3.6 and UTF-8"""
        with open("setup.cfg", mode="r", encoding="utf-8") as input_file:
            cfg = input_file.readlines()
        with open("setup.cfg", mode="w", encoding="ascii", errors="backslashreplace") as output_file:
            output_file.writelines(cfg)
