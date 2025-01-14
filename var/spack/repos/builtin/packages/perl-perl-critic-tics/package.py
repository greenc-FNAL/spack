# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlCriticTics(PerlPackage):
    """Policies for things that make me wince."""

    homepage = "https://github.com/rjbs/Perl-Critic-Tics"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Perl-Critic-Tics-0.009.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.009", sha256="7542662b56622f5d646b00068c8f9befbc16e462228a0cd47d54549d24eb7493")
    version("0.008", sha256="26bfa6dff571061c71e9914a71d90ae02e661bfac0943cf60ae5085c86766999")

    provides("perl-perl-critic-policy-tics-prohibitlonglines")
    provides("perl-perl-critic-policy-tics-prohibitmanyarrows")
    provides("perl-perl-critic-policy-tics-prohibitusebase")
    depends_on("perl-perl-critic-policy", type="run")
    depends_on("perl-perl-critic-utils", type="run")
    depends_on("perl-extutils-makemaker@6.30:", type="build")
    depends_on("perl-perl-critic-testutils", type=("build", "test"))
    depends_on("perl-perl-critic-violation", type="run")
