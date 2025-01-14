# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDevelCaller(PerlPackage):
    """Meatier versions of caller."""

    homepage = "https://cpan.metacpan.org/authors/id/R/RC/RCLAMP"
    url = "https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Devel-Caller-2.06.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("2.06", sha256="6a73ae6a292834255b90da9409205425305fcfe994b148dcb6d2d6ef628db7df")
    version("2.05", sha256="dcfb590044277e125e78f781a150198a94c89769af6faab8f544a916dfbb4388")

    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-padwalker@0.8:", type="run")
