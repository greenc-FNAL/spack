# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlHttpTinyMech(PerlPackage):
    """Wrap a WWW::Mechanize instance in an HTTP::Tiny compatible interface.."""

    homepage = "https://github.com/kentnl/HTTP-Tiny-Mech"
    url = "https://cpan.metacpan.org/authors/id/K/KE/KENTNL/HTTP-Tiny-Mech-1.001002.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version(
        "1.001.002",
        sha256="ed3b428307c678b9ddf27c180490c58d75da19b3d83c1269fd44a4054fed6c24",
        url="https://cpan.metacpan.org/authors/id/K/KE/KENTNL/HTTP-Tiny-Mech-1.001002.tar.gz",
    )
    version(
        "1.001.001",
        sha256="0bf8dd1850e0722f60ea56e5213d06f96326673300421f7cea5df735aab4590a",
        url="https://cpan.metacpan.org/authors/id/K/KE/KENTNL/HTTP-Tiny-Mech-1.001001.tar.gz",
    )

    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-http-response", type="test")
    depends_on("perl-www-mechanize", type="run")
    depends_on("perl-extutils-makemaker@7.0:", type=("build", "test"))
    depends_on("perl-http-request", type="run")
    depends_on("perl-http-tiny@0.22:", type=("run", "test"))
