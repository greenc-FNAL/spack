# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlWwwMechanize(PerlPackage):
    """Handy web browsing in a Perl object."""

    homepage = "https://github.com/libwww-perl/WWW-Mechanize"
    url = "https://cpan.metacpan.org/authors/id/S/SI/SIMBABQUE/WWW-Mechanize-2.15.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("2.15", sha256="91d0dc3235027d19fc485e93833ec92497bc508e31d391eb07ee664f988ca9b3")
    version("2.14", sha256="b7b07bbccc5a4554dd66888214ce9bc2dfd949782e33a2ebfb64a10e396cf3a6")

    provides("perl-www-mechanize-image")
    provides("perl-www-mechanize-link")
    depends_on("perl-compress-zlib", type="run")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-html-form@6.8:", type="run")
    depends_on("perl-html-headparser", type="run")
    depends_on("perl-html-tokeparser", type="run")
    depends_on("perl-html-treebuilder@5:", type="run")
    depends_on("perl-http-cookies", type="run")
    depends_on("perl-http-daemon@6.12:", type="test")
    depends_on("perl-http-request-common", type="run")
    depends_on("perl-http-request@1.30:", type="run")
    depends_on("perl-lwp", type="test")
    depends_on("perl-lwp-simple", type="test")
    depends_on("perl-lwp-useragent", type="run")
    depends_on("perl-path-tiny", type="test")
    depends_on("perl-scalar-util@1.14:", type="run")
    depends_on("perl-test-deep", type="test")
    depends_on("perl-test-exception", type="test")
    depends_on("perl-test-fatal", type="test")
    depends_on("perl-test-memory-cycle@1.6:", type="test")
    depends_on("perl-test-nowarnings@1.4:", type="test")
    depends_on("perl-test-output", type="test")
    depends_on("perl-test-taint@1.8:", type="test")
    depends_on("perl-test-warn", type="test")
    depends_on("perl-test-warnings", type="test")
    depends_on("perl-tie-refhash", type="run")
    depends_on("perl-uri", type="test")
    depends_on("perl-uri-escape", type="test")
    depends_on("perl-uri-file", type="run")
    depends_on("perl-uri-url", type="run")
    depends_on("perl@5.6:", type="run")
