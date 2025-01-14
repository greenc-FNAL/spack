# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlAck(PerlPackage):
    """A grep-like program for searching source code."""

    homepage = "https://beyondgrep.com/"
    url = "https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/ack-v3.6.0.tar.gz"

    license("Artistic-2.0", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("3.6.0", sha256="03144d1070649e92f6a1b7d20bdc535e2bb1ac258daabe482e9aa8277b48f005")
    version("3.5.0", sha256="66053e884e803387a02ddee0d68abf2a10239fab654364dab33287309a725521")

    provides("perl-app-ack")
    provides("perl-app-ack-configdefault")
    provides("perl-app-ack-configfinder")
    provides("perl-app-ack-configloader")
    provides("perl-app-ack-file")
    provides("perl-app-ack-files")
    provides("perl-app-ack-filter")
    provides("perl-app-ack-filter-collection")
    provides("perl-app-ack-filter-default")
    provides("perl-app-ack-filter-extension")
    provides("perl-app-ack-filter-extensiongroup")
    provides("perl-app-ack-filter-firstlinematch")
    provides("perl-app-ack-filter-inverse")
    provides("perl-app-ack-filter-is")
    provides("perl-app-ack-filter-isgroup")
    provides("perl-app-ack-filter-ispath")
    provides("perl-app-ack-filter-ispathgroup")
    provides("perl-app-ack-filter-match")
    provides("perl-app-ack-filter-matchgroup")
    depends_on("perl@5.10.1:", type="run")
    depends_on("perl-test-harness@2.50:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-file-next@1.18:", type="run")
    depends_on("perl-scalar-util", type="run")
    depends_on("perl-list-util", type="run")
