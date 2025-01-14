# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestMockrandom(PerlPackage):
    """Replaces random number generation with non-random number generation."""

    homepage = "https://github.com/dagolden/Test-MockRandom"
    url = "https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-MockRandom-1.01.tar.gz"

    license("Apache-2.0", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.01", sha256="2614930d84fc5deac39afbc1ee86ccd39b221507f27d4ee493ca26e5c921cce0")
    version("1.00", sha256="630bca40269d04520e39bb6579eb0399684cb17728702336ed1eb1542b7c2f97")

    depends_on("perl@5.6:", type="run")
    depends_on("perl-extutils-makemaker@6.17:", type="build")
    depends_on("perl-extutils-makemaker", type="test")
    depends_on("perl-list-util", type=("build", "test"))
