# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTypeTinyXs(PerlPackage):
    """Provides an XS boost for some of Type::Tiny's built-in type
    constraints."""

    homepage = "https://metacpan.org/release/Type-Tiny-XS"
    url = "https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-XS-0.022.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.022", sha256="bcc34a31f7dc1d30cc803889b5c8f90e4773b73b5becbdb3860f5abe7e22ff00")
    version("0.021", sha256="f7a9e216d1496744def402aa326620e13e73ad1ee7109cfbaeaac363d8eaf5df")

    provides("perl-type-tiny-xs-util")
    depends_on("perl@5.10.1:", type="run")
    depends_on("perl-extutils-makemaker@6.17:", type="build")
