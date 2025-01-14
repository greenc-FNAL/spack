# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlMinimumversion(PerlPackage):
    """Find a minimum required version of perl for Perl code."""

    homepage = "https://github.com/neilb/Perl-MinimumVersion"
    url = "https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Perl-MinimumVersion-1.40.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.40", sha256="7589a578cb60d70ca4755c395b3592b440a0cd6a1b074e4eceac93b031a1be90")
    version(
        "1.39-TRIAL", sha256="df936dbacd2dcf2850fae49a3cb766fa3364f8138a05eba0c7da43b63744d5e7"
    )

    provides("perl-perl-minimumversion-reason")
    depends_on("perl-params-util@0.25:", type="run")
    depends_on("perl-file-find-rule-perl", type="run")
    depends_on("perl-file-find-rule", type="run")
    depends_on("perl-ppix-regexp@0.33:", type="run")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-ppi@1.215:", type="run")
    depends_on("perl-ppi-util", type="run")
    depends_on("perl@5.6:", type="run")
    depends_on("perl-ppix-utils", type="run")
    depends_on("perl-list-util@1.20:", type="run")
