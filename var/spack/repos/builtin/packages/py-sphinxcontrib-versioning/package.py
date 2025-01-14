# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySphinxcontribVersioning(PythonPackage):
    """Sphinx extension that allows building versioned docs for self-hosting."""

    homepage = "https://github.com/Robpol86/sphinxcontrib-versioning"
    pypi = "sphinxcontrib-versioning/sphinxcontrib-versioning-2.2.1.tar.gz"

    license("MIT", checked_by="greenc-FNAL")

    maintainers("greenc-FNAL", "gartung", "marcmengel", "vitodb")

    version("2.2.1", sha256="1a5fe9b4e36020488d0d037fccc0b21aaf71b80425cad42ef4a5e5c3c193d3cd")

    depends_on("py-setuptools", type="build")

    depends_on("py-click", type=("build", "run"))
    depends_on("py-colorclass", type=("build", "run"))
