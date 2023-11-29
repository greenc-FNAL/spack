# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMystParser(PythonPackage):
    """A Sphinx and Docutils extension to parse MyST, a rich and
    extensible flavour of Markdown for authoring technical and
    scientific documentation.
    """

    homepage = "https://github.com/executablebooks/MyST-Parser"
    documentation = "https://myst-parser.readthedocs.io/en/latest/"
    keywords = ["markdown", "lexer", "parser", "development", "docutils", "sphinx"]
    pypi = "myst-parser/myst-parser-0.18.0.tar.gz"

    maintainers("chissg", "gartung", "marcmengel", "vitodb")

    version("1.0.0", sha256="502845659313099542bd38a2ae62f01360e7dd4b1310f025dd014dfc0439cdae")
    version("0.18.1", sha256="79317f4bb2c13053dd6e64f9da1ba1da6cd9c40c8a430c447a7b146a594c246d")
    version("0.18.0", sha256="739a4d96773a8e55a2cacd3941ce46a446ee23dcd6b37e06f73f551ad7821d86")

    depends_on("python@3.7:", when="@:1", type=("build", "run"))
    depends_on("python@3.8:", when="@2:", type=("build", "run"))

    depends_on("py-flit-core@3.4:3", type="build")

    depends_on("py-docutils@0.15:0.19", when="@:1", type=("build", "run"))
    depends_on("py-docutils@0.15:0.20", when="@2:", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-markdown-it-py@1.0.0:2", when="@:1", type=("build", "run"))
    depends_on("py-markdown-it-py@3", when="@2:", type=("build", "run"))
    depends_on("py-mdit-py-plugins@0.3.1:0", when="@0", type=("build", "run"))
    depends_on("py-mdit-py-plugins@0.3.4:0", when="@1", type=("build", "run"))
    depends_on("py-mdit-py-plugins@0.4:0", when="@2:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-sphinx@4.0.0:5", when="@0", type=("build", "run"))
    depends_on("py-sphinx@5.0.0:6", when="@1", type=("build", "run"))
    depends_on("py-sphinx@6.0.0:7", when="@2:", type=("build", "run"))
    depends_on("py-typing-extensions", when="^python@:3.7", type=("build", "run"))
