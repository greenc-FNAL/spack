# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlCriticLax(PerlPackage):
    """Policies that let you slide on common exceptions."""

    homepage = "https://github.com/rjbs/Perl-Critic-Lax"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Perl-Critic-Lax-0.013.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.013", sha256="3f5619c209f93676e2fcdcd2990a27a5d77d2b0e60dcbdcd2680617355fd4620")
    version("0.012", sha256="47772ddbdd3c6ab00571c0ed8e95aeace705f725c650a572f060c30f7a96227a")

    provides("perl-perl-critic-policy-lax-prohibitcomplexmappings-linesnotstatements")
    provides("perl-perl-critic-policy-lax-prohibitemptyquotes-exceptasfallback")
    provides("perl-perl-critic-policy-lax-prohibitleadingzeros-exceptchmod")
    provides("perl-perl-critic-policy-lax-prohibitstringyeval-exceptforrequire")
    provides("perl-perl-critic-policy-lax-requireconstantonleftsideofequality-excepteq")
    provides("perl-perl-critic-policy-lax-requireendwithtrueconst")
    provides("perl-perl-critic-policy-lax-requireexplicitpackage-exceptforpragmata")
    depends_on("perl-readonly", type="run")
    depends_on("perl-perl-critic-policy", type="run")
    depends_on("perl-perl-critic-utils", type="run")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-perl-critic-testutils", type=("build", "test"))
    depends_on("perl-perl-critic-policy-valuesandexpressions-prohibitleadingzeros", type="run")
    depends_on("perl-perl-critic@1.88:", type="run")
