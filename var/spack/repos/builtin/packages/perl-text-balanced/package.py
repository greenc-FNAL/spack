# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTextBalanced(PerlPackage):
    """Extract delimited text sequences from strings.."""

    homepage = "https://cpan.metacpan.org/authors/id/S/SH/SHAY"
    url = "https://cpan.metacpan.org/authors/id/S/SH/SHAY/Text-Balanced-2.06.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("2.06", sha256="773e0f0f21c0cb2cf664cee6ba28ff70259babcc892f9b650f9cbda00be092ad")
    version("2.05", sha256="3a6f3fbcc6cb5406964b2e332688bae3c2595436d03ddb25ee6703a47a98977d")

    provides("perl-text-balanced-errormsg")
    provides("perl-text-balanced-extractor")
    depends_on("perl@5.8.1:", type=("build", "run"))
    depends_on("perl-extutils-makemaker@6.64:", type="build")
