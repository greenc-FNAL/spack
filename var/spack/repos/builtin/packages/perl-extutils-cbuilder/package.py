# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlExtutilsCbuilder(PerlPackage):
    """Compile and link C code for Perl modules."""

    homepage = "http://search.cpan.org/dist/ExtUtils-CBuilder"
    url = "https://cpan.metacpan.org/authors/id/A/AM/AMBS/ExtUtils-CBuilder-0.280236.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version(
        "0.28.2.36",
        url="https://cpan.metacpan.org/authors/id/A/AM/AMBS/ExtUtils-CBuilder-0.280236.tar.gz",
        sha256="abc21827eb8a513171bf7fdecefce9945132cb76db945036518291f607b1491f",
    )
    version(
        "0.28.2.35",
        url="https://cpan.metacpan.org/authors/id/A/AM/AMBS/ExtUtils-CBuilder-0.280235.tar.gz",
        sha256="a0f454d84eb599bf0c11b976ab2ce39ada49bf84c323c7a53fe9f8941ee9378a",
    )

    provides("perl-extutils-cbuilder-base")
    provides("perl-extutils-cbuilder-platform-unix")
    provides("perl-extutils-cbuilder-platform-vms")
    provides("perl-extutils-cbuilder-platform-windows")
    provides("perl-extutils-cbuilder-platform-windows-bcc")
    provides("perl-extutils-cbuilder-platform-windows-gcc")
    provides("perl-extutils-cbuilder-platform-windows-msvc")
    provides("perl-extutils-cbuilder-platform-aix")
    provides("perl-extutils-cbuilder-platform-android")
    provides("perl-extutils-cbuilder-platform-cygwin")
    provides("perl-extutils-cbuilder-platform-darwin")
    provides("perl-extutils-cbuilder-platform-dec-osf")
    provides("perl-extutils-cbuilder-platform-os2")
    depends_on("perl-extutils-makemaker@6.30:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-perl-ostype@1:", type="run")
