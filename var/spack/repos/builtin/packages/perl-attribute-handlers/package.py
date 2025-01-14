# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlAttributeHandlers(PerlPackage):
    """Simpler definition of attribute handlers."""

    homepage = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Attribute-Handlers-0.99.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.99", sha256="937ea3ebfc9b14f4a4148bf3c32803709edbd12a387137a26370b38ee1fc9835")
    version("0.98", sha256="7d53613496faf6f25c41dfb870b3aca197ed7208252b6b4fd7a39a57511d401a")

    depends_on("perl-extutils-makemaker", type="build")
