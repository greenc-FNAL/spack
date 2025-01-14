# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlHtmlFormatter(PerlPackage):
    """Base class for HTML formatters."""

    homepage = "https://metacpan.org/release/HTML-Formatter"
    url = "https://cpan.metacpan.org/authors/id/N/NI/NIGELM/HTML-Formatter-2.16.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("2.16", sha256="cb0a0dd8aa5e8ba9ca214ce451bf4df33aa09c13e907e8d3082ddafeb30151cc")
    version("2.14", sha256="d28eeeab48ab5f7bfcc73cc106b0f756073d98d48dfdb91ca2951f832f8e035e")

    depends_on("perl-html-element@3.15:", type=("build", "test"))
    provides("perl-html-formatmarkdown")
    provides("perl-html-formatps")
    provides("perl-html-formatrtf")
    provides("perl-html-formattext")
    depends_on("perl-font-metrics-timesbolditalic", type="run")
    depends_on("perl-test-warnings", type=("build", "test"))
    depends_on("perl-font-metrics-helvetica", type="run")
    depends_on("perl-font-metrics-timesroman", type="run")
    depends_on("perl-html-element@3.15:", type="run")
    depends_on("perl-font-metrics-courieroblique", type="run")
    depends_on("perl-font-metrics-helveticaoblique", type="run")
    depends_on("perl-font-metrics-courierboldoblique", type="run")
    depends_on("perl-font-metrics-timesbold", type="run")
    depends_on("perl-font-metrics-helveticabold", type="run")
    depends_on("perl-font-metrics-timesitalic", type="run")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-font-metrics-courier", type="run")
    depends_on("perl@5.8:", type="run")
    depends_on("perl-file-slurper", type=("build", "test"))
    depends_on("perl-font-metrics-courierbold", type="run")
    depends_on("perl-font-metrics-helveticaboldoblique", type="run")
    depends_on("perl-html-treebuilder", type="run")
    depends_on("perl-data-dumper", type="run")
