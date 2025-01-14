# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlFilter(PerlPackage):
    """Source Filters."""

    homepage = "https://cpan.metacpan.org/authors/id/R/RU/RURBAN"
    url = "https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Filter-1.64.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.64", sha256="13e7fb7e1d326598e3660103cf1974bee9f690ac5b43b339f2c022f2b5fcef2c")
    version("1.63", sha256="b667f5693e4608d908e2cf4527fa84f2a858f015b16c344b6961b0090f63670c")

    provides("perl-filter-util-call")
    provides("perl-filter-util-exec")
    provides("perl-filter-cpp")
    provides("perl-filter-decrypt")
    provides("perl-filter-exec")
    provides("perl-filter-m4")
    provides("perl-filter-sh")
    provides("perl-filter-tee")
    depends_on("perl-filter-simple@0.88:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
