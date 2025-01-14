# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlCriticStrictersubs(PerlPackage):
    """Perl::Critic plugin for stricter subroutine checking."""

    homepage = "http://perlcritic.com"
    url = "https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Perl-Critic-StricterSubs-0.06.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.06", sha256="bdf438b7b29c6699fbdea317400ae4b8d28a2078b21c51c9afe8e06c96c9ca77")

    depends_on("perl-module-build", type="build")

    provides("perl-perl-critic-policy-modules-requireexplicitinclusion")
    provides("perl-perl-critic-policy-subroutines-prohibitcallstoundeclaredsubs")
    provides("perl-perl-critic-policy-subroutines-prohibitcallstounexportedsubs")
    provides("perl-perl-critic-policy-subroutines-prohibitexportingundeclaredsubs")
    provides("perl-perl-critic-policy-subroutines-prohibitqualifiedsubdeclarations")
    provides("perl-perl-critic-strictersubs-utils")
    depends_on("perl-file-pathlist", type="run")
    depends_on("perl@5.6.1:", type="run")
    depends_on("perl-module-build@0.4:", type="build")
    depends_on("perl-perl-critic-policy@1.82:", type="run")
    depends_on("perl-perl-critic-utils@1.82:", type="run")
    depends_on("perl-perl-critic-testutils@1.82:", type=("build", "test"))
    depends_on("perl-ppi-document", type="run")
    depends_on("perl-list-moreutils", type="run")
