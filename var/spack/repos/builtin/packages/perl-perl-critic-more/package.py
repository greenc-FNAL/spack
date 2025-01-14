# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlCriticMore(PerlPackage):
    """Supplemental policies for Perl::Critic."""

    homepage = "http://perlcritic.com"
    url = "https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Perl-Critic-More-1.003.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.003", sha256="69e2acff61b7bead745721991e2b83c88624ae8239d4371a785a3ce2d967187b")
    version("1.002", sha256="71cd154f311cb59df47df413efde460fa93b543eb6e7293080adfd3cc3050f8c")

    depends_on("perl-module-build", type="build")

    provides("perl-perl-critic-policy-codelayout-requireascii")
    provides("perl-perl-critic-policy-editor-requireemacsfilevariables")
    provides("perl-perl-critic-policy-errorhandling-requireuseofexceptions")
    provides("perl-perl-critic-policy-modules-perlminimumversion")
    provides("perl-perl-critic-policy-modules-requireperlversion")
    provides("perl-perl-critic-policy-valuesandexpressions-requireconstantonleftsideofequality")
    provides("perl-perl-critic-policy-valuesandexpressions-restrictlongstrings")
    depends_on("perl-readonly@1.3:", type="run")
    depends_on("perl-module-build@0.4:", type="build")
    depends_on("perl-perl-minimumversion@0.14:", type="run")
    depends_on("perl-perl-critic@1.98:", type="run")
