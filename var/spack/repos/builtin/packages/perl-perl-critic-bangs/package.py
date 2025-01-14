# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlCriticBangs(PerlPackage):
    """Perl::Critic::Bangs - A collection of policies for Perl::Critic."""

    homepage = "https://cpan.metacpan.org/authors/id/P/PE/PETDANCE"
    url = "https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Perl-Critic-Bangs-1.12.tar.gz"

    license("Artistic-2.0", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.12", sha256="73242b27da2feb601e4a47e7975d864df7279317f1b0565474be3cfc31bfa119")
    version("1.11_03", sha256="420b5cd5faf96405d1040f3e896e8811a691ba73ba3b75058b6ac4efc6e1f27a")

    provides("perl-perl-critic-policy-bangs-prohibitbitwiseoperators")
    provides("perl-perl-critic-policy-bangs-prohibitcommentedoutcode")
    provides("perl-perl-critic-policy-bangs-prohibitdebuggingmodules")
    provides("perl-perl-critic-policy-bangs-prohibitflagcomments")
    provides("perl-perl-critic-policy-bangs-prohibitnoplan")
    provides("perl-perl-critic-policy-bangs-prohibitnumberednames")
    provides("perl-perl-critic-policy-bangs-prohibitrefprotoorproto")
    provides("perl-perl-critic-policy-bangs-prohibituselessregexmodifiers")
    provides("perl-perl-critic-policy-bangs-prohibitvaguenames")
    depends_on("perl-readonly", type="run")
    depends_on("perl-perl-critic-policyfactory", type="run")
    depends_on("perl-test-perl-critic@1.1:", type="run")
    depends_on("perl-perl-critic-policyparameter", type="run")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-ppi-cache", type="run")
    depends_on("perl-perl-critic-violation", type="run")
    depends_on("perl-perl-critic@1.122:", type="run")
    depends_on("perl-perl-critic-policy", type="run")
    depends_on("perl-perl-critic-utils", type="run")
    depends_on("perl-perl-critic-testutils", type="run")
    depends_on("perl-ppi-document", type="run")
    depends_on("perl-perl-critic-userprofile", type="run")
