# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTieRefhash(PerlPackage):
    """Use references as hash keys."""

    homepage = "https://github.com/karenetheridge/Tie-RefHash"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/Tie-RefHash-1.40.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.40", sha256="5acf1f518d2fb5f620caad7a1b2ff1f6f7516fef8f40ba6b743eec8b96927ed7")

    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-scalar-util", type="run")
    depends_on("perl-data-dumper", type="test")
