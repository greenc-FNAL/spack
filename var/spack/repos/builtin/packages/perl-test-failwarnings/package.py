# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestFailwarnings(PerlPackage):
    """Add test failures if warnings are caught."""

    homepage = "https://github.com/dagolden/Test-FailWarnings"
    url = "https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-FailWarnings-0.008.tar.gz"

    license("Apache-2.0", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.008", sha256="da34ef9029f6849d6026201d49127d054ee6ac4b979c82210315f5721964a96f")
    version("0.007", sha256="fe3a5d3be7bd8477248043df947af175f8f8c0ce302cdb21e19037bdf1ab75e0")

    depends_on("perl@5.8.1:", type="run")
    depends_on("perl-extutils-makemaker@6.17:", type="build")
    depends_on("perl-extutils-makemaker", type="test")
    depends_on("perl-list-util", type=("build", "test"))
    depends_on("perl-capture-tiny@0.12:", type=("build", "test"))
