# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlUnicodeUtf8(PerlPackage):
    """Encoding and decoding of UTF-8 encoding form."""

    homepage = "https://cpan.metacpan.org/authors/id/C/CH/CHANSEN"
    url = "https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/Unicode-UTF8-0.62.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.62", sha256="fa8722d0b74696e332fddd442994436ea93d3bfc7982d4babdcedfddd657d0f6")
    version("0.61", sha256="5ee155a8af856ac9b24819cf153592a13338651440478cb1dbf0e7f8e566676f")

    depends_on("perl-test-fatal@0.6:", type="build")
    depends_on("perl@5.8.1:", type="run")
    depends_on("perl-extutils-makemaker@6.59:", type="build")
