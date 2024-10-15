# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTimedate(PerlPackage):
    """The parser contained here will only parse absolute dates, if you want a
    date parser that can parse relative dates then take a look at the Time
    modules by David Muir on CPAN."""

    homepage = "https://metacpan.org/release/TimeDate"
    url = "https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/TimeDate-2.33.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("2.33", sha256="c0b69c4b039de6f501b0d9f13ec58c86b040c1f7e9b27ef249651c143d605eb2")
    version("2.30", sha256="75bd254871cb5853a6aa0403ac0be270cdd75c9d1b6639f18ecba63c15298e86")

    provides("perl-date-format@2.24")
    provides("perl-date-format-generic")
    provides("perl-date-language@1.10")
    provides("perl-date-language-afar@0.99")
    provides("perl-date-language-amharic@1.00")
    provides("perl-date-language-austrian@1.01")
    provides("perl-date-language-brazilian@1.01")
    provides("perl-date-language-bulgarian@1.01")
    provides("perl-date-language-chinese@1.00")
    provides("perl-date-language-chinese-gb@1.01")
    provides("perl-date-language-czech@1.01")
    provides("perl-date-language-danish@1.01")
    provides("perl-date-language-dutch@1.02")
    provides("perl-date-language-english@1.01")
    provides("perl-date-language-finnish@1.01")
    provides("perl-date-language-french@1.04")
    provides("perl-date-language-gedeo@0.99")
    provides("perl-date-language-german@1.02")
    provides("perl-date-language-greek@1.00")
    provides("perl-date-language-hungarian@1.01")
    provides("perl-date-language-icelandic@1.01")
    provides("perl-date-language-italian@1.01")
    provides("perl-date-language-norwegian@1.01")
    provides("perl-date-language-occitan@1.04")
    provides("perl-date-language-oromo@0.99")
    provides("perl-date-language-romanian@1.01")
    provides("perl-date-language-russian@1.01")
    provides("perl-date-language-russian-cp1251@1.01")
    provides("perl-date-language-russian-koi8r@1.01")
    provides("perl-date-language-sidama@0.99")
    provides("perl-date-language-somali@0.99")
    provides("perl-date-language-spanish@1.00")
    provides("perl-date-language-swedish@1.01")
    provides("perl-date-language-tigrinya@1.00")
    provides("perl-date-language-tigrinyaeritrean@1.00")
    provides("perl-date-language-tigrinyaethiopian@1.00")
    provides("perl-date-language-turkish@1.0")
    provides("perl-date-parse")
    provides("perl-time-zone@2.24")

    depends_on("perl-extutils-makemaker", type="build")

    def url_for_version(self, version):
        if self.spec.satisfies("@2.31:"):
            return f"https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/TimeDate-{version}.tar.gz"
        else:
            return f"https://cpan.metacpan.org/authors/id/G/GB/GBARR/TimeDate-{version}.tar.gz"
