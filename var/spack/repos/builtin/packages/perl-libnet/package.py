# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlLibnet(PerlPackage):
    """Collection of network protocol modules."""

    homepage = "https://cpan.metacpan.org/authors/id/S/SH/SHAY"
    url = "https://cpan.metacpan.org/authors/id/S/SH/SHAY/libnet-3.14.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("3.14", sha256="153c8eb8ef0f19cf2c631d5b45d05de98516937f34e261125ef242fba1fe2ea4")
    version("3.13", sha256="5a35fb1f2d4aa291680eb1af38899fab453c22c28e71f7c7bd3747b5a3db348c")

    depends_on("perl@5.8.1:", type=("build", "run"))
    depends_on("perl-extutils-makemaker@6.64:", type="build")
    depends_on("perl-time-local", type="run")
