# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlWwwMechanizeCached(PerlPackage):
    """Cache response to be polite."""

    homepage = "https://github.com/libwww-perl/WWW-Mechanize-Cached"
    url = "https://cpan.metacpan.org/authors/id/O/OA/OALDERS/WWW-Mechanize-Cached-1.56.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.56", sha256="a18b0706aac202604adc575b6be6b8ae26b373a9d43d8da59c826d7d300151dd")
    version("1.55", sha256="3ab16463beede3061db7b7d3c66ea9536f02b737467cc6b1172aa08302d9fb60")

    depends_on("perl-test-warnings", type="test")
    depends_on("perl-data-dump", type="run")
    depends_on("perl-lwp-useragent@6.66:", type="run")
    depends_on("perl-http-response", type="test")
    depends_on("perl-test-requiresinternet", type="test")
    depends_on("perl-path-tiny", type="test")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-uri-file", type="test")
    depends_on("perl-test-needs", type="test")
    depends_on("perl-namespace-clean", type="run")
    depends_on("perl-moo@1.4.5:", type="run")
    depends_on("perl-test-fatal", type="test")
    depends_on("perl@5.6:", type="build")
    depends_on("perl@5.8:", type=("run", "test"))
    depends_on("perl-moox-types-mooselike-base", type="run")
    depends_on("perl-cache-filecache", type=("run", "test"))
    depends_on("perl-www-mechanize", type="run")
    depends_on("perl-module-runtime", type="run")
    depends_on("perl-chi", type=("run", "test"))
    depends_on("perl-http-request", type="test")
