# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlClassAccessorLite(PerlPackage):
    """A minimalistic variant of Class::Accessor."""

    homepage = "https://cpan.metacpan.org/authors/id/K/KA/KAZUHO"
    url = "https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Class-Accessor-Lite-0.08.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.08", sha256="75b3b8ec8efe687677b63f0a10eef966e01f60735c56656ce75cbb44caba335a")
    version("0.07", sha256="a8aaaaf32a64e9ff89dbc4ef8a55d6197f5c161b8fc8d64219eef9ea173971d1")

    depends_on("perl-extutils-makemaker@6.36:", type="build")

    def setup_build_environment(self, env):
        env.prepend_path("PERL5LIB", self.stage.source_path)
