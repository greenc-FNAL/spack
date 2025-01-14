# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPerlCriticStorable(PerlPackage):
    """Policy for Storable.pm."""

    homepage = "https://cpan.metacpan.org/authors/id/M/MA/MATTD"
    url = "https://cpan.metacpan.org/authors/id/M/MA/MATTD/Perl-Critic-Storable-0.01.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("0.01", sha256="11d1a5417b60c09c78ecb187cea84a95daf5fd47aa44810fa6ceff1879b1ad61")

    provides("perl-perl-critic-policy-storable-prohibitstoreorfreeze")
    depends_on("perl-perl-critic", type="run")
