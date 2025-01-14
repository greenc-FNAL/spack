# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PerlPerlCriticPetpeevesJtrammell(PerlPackage):
    """Policies to prohibit/require my pet peeves."""

    homepage = "https://cpan.metacpan.org/authors/id/J/JT/JTRAMMELL"
    url = "https://cpan.metacpan.org/authors/id/J/JT/JTRAMMELL/Perl-Critic-PetPeeves-JTRAMMELL-0.04.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.04", sha256="fb931eb3434b6b75339d079a469f7a389269df155f46ee5e7cc60c2ebbae4a04")
    version("0.03", sha256="756671be54d026aa018527285d32205c83080fe32d0d60bb947c254455a46e18")

    provides("perl-perl-critic-policy-variables-prohibituselessinitialization@0.02")
    depends_on("perl-module-build@0.35:", type="build")
    depends_on("perl-perl-critic-policy", type="run")
    depends_on("perl-perl-critic-utils", type="run")
    depends_on("perl-perl-critic-config", type="build")

    @run_before("configure")
    def remove_bad_Makefile_PL(self):
        os.remove("Makefile.PL")
