# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlExtutilsParsexs(PerlPackage):
    """Converts Perl XS code into C code."""

    homepage = "https://github.com/Perl/perl5"
    url = "https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/ExtUtils-ParseXS-3.44.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("3.44", sha256="77effdf31af36ef656f09aa7c15356d238dab6d1afaa7278ae15c1b6bcf86266")

    provides("perl-extutils-parsexs-constants")
    provides("perl-extutils-parsexs-countlines")
    provides("perl-extutils-parsexs-eval")
    provides("perl-extutils-parsexs-utilities")
    provides("perl-extutils-typemaps")
    provides("perl-extutils-typemaps-cmd")
    provides("perl-extutils-typemaps-inputmap")
    provides("perl-extutils-typemaps-outputmap")
    provides("perl-extutils-typemaps-type")
    depends_on("perl-extutils-cbuilder", type="run")
    depends_on("perl-dynaloader", type="run")
    depends_on("perl-extutils-makemaker@6.46:", type=("build", "run"))
