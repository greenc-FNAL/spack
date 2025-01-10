# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAutodocsumm(PythonPackage):
    """Extended sphinx autodoc including automatic autosummaries."""

    homepage = "https://github.com/Chilipp/autodocsumm"
    pypi = "autodocsumm/autodocsumm-0.2.11.tar.gz"

    maintainers("gartung", "greenc-FNAL", "LydDeb", "marcmengel")

    license("Apache-2.0")

    version("0.2.14", sha256="2839a9d4facc3c4eccd306c08695540911042b46eeafcdc3203e6d0bab40bc77")
    version("0.2.11", sha256="183212bd9e9f3b58a96bb21b7958ee4e06224107aa45b2fd894b61b83581b9a9")

    depends_on("py-setuptools@61.0:", type="build")
    depends_on("py-versioneer+toml", type="build")
    depends_on("py-sphinx@2.2:7", when="@0.2.11", type=("build", "run"))
    depends_on("py-sphinx@4:8", when="@0.2.14:", type=("build", "run"))
