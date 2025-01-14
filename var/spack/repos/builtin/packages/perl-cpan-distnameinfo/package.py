# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCpanDistnameinfo(PerlPackage):
    """Extract distribution name and version from a distribution filename."""  # AUTO-CPAN2Spack

    homepage = "https://cpan.metacpan.org/authors/id/G/GB/GBARR"  # AUTO-CPAN2Spack
    url = "https://cpan.metacpan.org/authors/id/G/GB/GBARR/CPAN-DistnameInfo-0.12.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("chissg", "gartung", "marcmengel", "vitodb")  # AUTO-CPAN2Spack

    version("0.12", sha256="2f24fbe9f7eeacbc269d35fc61618322fc17be499ee0cd9018f370934a9f2435")
    version("0.11", sha256="8796af6350a8113451a6f6459d2cd31fdb859f9f3784a5bb568e628c8b5e92ea")

    depends_on("perl-extutils-makemaker", type="build")  # AUTO-CPAN2Spack
