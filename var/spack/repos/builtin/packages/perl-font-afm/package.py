# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlFontAfm(PerlPackage):
    """Interface to Adobe Font Metrics files."""

    homepage = "https://cpan.metacpan.org/authors/id/G/GA/GAAS"
    url = "https://cpan.metacpan.org/authors/id/G/GA/GAAS/Font-AFM-1.20.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("1.20", sha256="32671166da32596a0f6baacd0c1233825a60acaf25805d79c81a3f18d6088bc1")
    version("1.19", sha256="6b77e90b8922e899ed75bb77b779f6aba3870736f1edd553e94cb219c7bf02a0")

    provides("perl-font-metrics-courier")
    provides("perl-font-metrics-courierbold")
    provides("perl-font-metrics-courierboldoblique")
    provides("perl-font-metrics-courieroblique")
    provides("perl-font-metrics-helvetica")
    provides("perl-font-metrics-helveticabold")
    provides("perl-font-metrics-helveticaboldoblique")
    provides("perl-font-metrics-helveticaoblique")
    provides("perl-font-metrics-timesbold")
    provides("perl-font-metrics-timesbolditalic")
    provides("perl-font-metrics-timesitalic")
    provides("perl-font-metrics-timesroman")
