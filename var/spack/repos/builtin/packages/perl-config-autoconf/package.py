# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlConfigAutoconf(PerlPackage):
    """A module to implement some of AutoConf macros in pure perl."""

    homepage = "https://metacpan.org/release/Config-AutoConf"
    url = "https://cpan.metacpan.org/authors/id/A/AM/AMBS/Config-AutoConf-0.320.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.320", sha256="bb57a958ef49d3f7162276dae14a7bd5af43fd1d8513231af35d665459454023")

    depends_on("perl-extutils-cbuilder@0.23:", type=("build", "test"))
    depends_on("perl-extutils-cbuilder@0.28.2.20:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-file-slurper", type="run")
    depends_on("perl-scalar-util@1.18:", type="run")
    depends_on("perl-capture-tiny", type="run")
