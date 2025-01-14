# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlHtmlTree(PerlPackage):
    """Work with HTML in a DOM-like tree structure."""

    homepage = "https://cpan.metacpan.org/authors/id/K/KE/KENTNL"
    url = "https://cpan.metacpan.org/authors/id/K/KE/KENTNL/HTML-Tree-5.07.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version(
        "5.910-TRIAL", sha256="3f15e318605684c44436a4276e340088edf11f5c5e94f12e3a1ed15602a673d3"
    )  # Pre-release.
    version(
        "5.07",
        sha256="f0374db84731c204b86c1d5b90975fef0d30a86bd9def919343e554e31a9dbbf",
        preferred=True,
    )
    version("5.06", sha256="9c36eb19cbdf9a5906c858948ca51c35bd7561f52cc18c43281acbe57327536e")

    depends_on("perl-module-build", type="build")

    provides("perl-html-assubs")
    provides("perl-html-element")
    provides("perl-html-element-traverse")
    provides("perl-html-parse")
    provides("perl-html-treebuilder")
    #    depends_on("perl-html-formattext", type="run")
    depends_on("perl-lwp-useragent@5.815:", type="run")
    depends_on("perl-html-tagset@3.2:", type="run")
    depends_on("perl-uri-file", type=("build", "test"))
    depends_on("perl-test-fatal", type=("build", "test"))
    depends_on("perl@5.8:", type="run")
    depends_on("perl-module-build@0.28.8:", type="build")
    depends_on("perl-test-leaktrace", type=("build", "test"))
    depends_on("perl-scalar-util", type="run")
    depends_on("perl-html-parser@3.46:", type="run")
    depends_on("perl-html-entities", type="run")
