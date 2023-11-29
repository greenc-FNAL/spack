# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PySphinxTabs(PythonPackage):
    """Create tabbed content in Sphinx documentation when building HTML."""

    homepage = "https://github.com/executablebooks/sphinx-tabs"
    pypi = "sphinx-tabs/sphinx-tabs-3.2.0.tar.gz"

    maintainers("schmitts")

    version("3.4.4", sha256="f1b72c4f23d1ba9cdcaf880fd883524bc70689f561b9785719b8b3c3c5ed0aca")
    version("3.2.0", sha256="33137914ed9b276e6a686d7a337310ee77b1dae316fdcbce60476913a152e0a4")

    depends_on("python@3.6:3", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-sphinx@2:4", when="@:3.2", type=("build", "run"))
    depends_on("py-sphinx", type=("build", "run"))
    depends_on("py-pygments", type=("build", "run"))
    depends_on("py-docutils@0.16:", when="@:3.2", type=("build", "run"))
    depends_on("py-docutils@0.18:", when="@3.4.4:", type=("build", "run"))
