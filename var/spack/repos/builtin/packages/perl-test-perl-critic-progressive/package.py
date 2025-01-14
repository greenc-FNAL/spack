# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestPerlCriticProgressive(PerlPackage):
    """Encourage Perl::Critic conformance over time."""

    homepage = "http://perlcritic.com"
    url = "https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Test-Perl-Critic-Progressive-0.03.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.03", sha256="665d717b4a4c35077b703115090aaa64f24ae12c6193674c8a096f031bc15b36")
    version("0.02", sha256="be23f3d422aa02dff48fbb18201e8c1c48d7e32ec2e11020c4c069d39e857141")

    depends_on("perl-module-build", type="build")

    depends_on("perl-perl-critic-utils@1.82:", type="run")
    depends_on("perl-perl-critic@1.82:", type="run")
    depends_on("perl-data-dumper", type="run")
