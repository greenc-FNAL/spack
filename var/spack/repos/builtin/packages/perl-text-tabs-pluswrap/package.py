# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTextTabsPluswrap(PerlPackage):
    """Expand tabs and do simple line wrapping."""

    homepage = "https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE"
    url = "https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/Text-Tabs+Wrap-2021.0814.tar.gz"

    license("Unknown", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("2021.0814", sha256="30bbea13a5f5ef446b676b4493644df0ea19fc6a70ff649a8beb64571dbf6dfa")

    provides("perl-text-tabs")
    provides("perl-text-wrap")
    depends_on("perl@5.6:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
