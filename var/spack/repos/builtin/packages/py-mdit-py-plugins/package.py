# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyMditPyPlugins(PythonPackage):
    """Collection of core plugins for markdown-it-py"""

    homepage = "https://github.com/executablebooks/mdit-py-plugins/"
    git = "https://github.com/executablebooks/mdit-py-plugins/"
    pypi = "mdit-py-plugins/mdit-py-plugins-0.3.5.tar.gz"

    version("0.4.0", sha256="d8ab27e9aed6c38aa716819fedfde15ca275715955f8a185a8e1cf90fb1d2c1b")
    version("0.3.5", sha256="eee0adc7195e5827e17e02d2a258a2ba159944a0748f59c5099a4a27f78fcf6a")
    version("0.3.4", sha256="3278aab2e2b692539082f05e1243f24742194ffd92481f48844f057b51971283")
    version("0.3.3", sha256="5cfd7e7ac582a594e23ba6546a2f406e94e42eb33ae596d0734781261c251260")
    version("0.3.2", sha256="c37ca25a4a5244b41cc3b34b9d7762a96ee0416dd43efaa837304d592a84995f")
    version("0.3.1", sha256="3fc13298497d6e04fe96efdd41281bfe7622152f9caa1815ea99b5c893de9441")
    version("0.3.0", sha256="ecc24f51eeec6ab7eecc2f9724e8272c2fb191c2e93cf98109120c2cace69750")
    version("0.2.8", sha256="5991cef645502e80a5388ec4fc20885d2313d4871e8b8e320ca2de14ac0c015f")

    depends_on("py-flit-core@3.4:3", when="@0.3.1:", type="build")
    depends_on("py-setuptools", when="@:0.3.0", type="build")

    depends_on("python@3.8:3", when="@0.4.0:", type=("build", "run"))
    depends_on("python@3.7:3", when="@0.3.1:0.3", type=("build", "run"))
    depends_on("python@3.6:3", when="@0.2.8", type=("build", "run"))

    depends_on("py-markdown-it-py@1.0:3", when="@0.4.0:", type=("build", "run"))
    depends_on("py-markdown-it-py@1.0:2", when="@0.3.1:0.3", type=("build", "run"))
    depends_on("py-markdown-it-py@1.0:1", when="@0.2.8", type=("build", "run"))

    def url_for_version(self, version):
        if version >= Version("0.4.0"):
            separator = "_"
        else:
            separator = "-"
        return (
            "https://files.pythonhosted.org/packages/source/m/mdit-py-plugins/"
            f"mdit{separator}py{separator}plugins-{version}.tar.gz"
        )
