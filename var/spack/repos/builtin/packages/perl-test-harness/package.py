# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlTestHarness(PerlPackage):
    """Contributing to TAP::Harness."""

    homepage = "http://testanything.org/"
    url = "https://cpan.metacpan.org/authors/id/L/LE/LEONT/Test-Harness-3.44.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("3.44", sha256="7eb591ea6b499ece6745ff3e80e60cee669f0037f9ccbc4e4511425f593e5297")
    version("3.43_06", sha256="14fdd5b127d64fdc73c1e39c6bdc568370a4773698eaf299ed7c7ab933f75535")

    provides("perl-app-prove")
    provides("perl-app-prove-state")
    provides("perl-app-prove-state-result")
    provides("perl-app-prove-state-result-test")
    provides("perl-tap-base")
    provides("perl-tap-formatter-base")
    provides("perl-tap-formatter-color")
    provides("perl-tap-formatter-console")
    provides("perl-tap-formatter-console-parallelsession")
    provides("perl-tap-formatter-console-session")
    provides("perl-tap-formatter-file")
    provides("perl-tap-formatter-file-session")
    provides("perl-tap-formatter-session")
    provides("perl-tap-harness")
    provides("perl-tap-harness-env")
    provides("perl-tap-object")
    provides("perl-tap-parser")
    provides("perl-tap-parser-aggregator")
    provides("perl-tap-parser-grammar")
    provides("perl-tap-parser-iterator")
    provides("perl-tap-parser-iterator-array")
    provides("perl-tap-parser-iterator-process")
    provides("perl-tap-parser-iterator-stream")
    provides("perl-tap-parser-iteratorfactory")
    provides("perl-tap-parser-multiplexer")
    provides("perl-tap-parser-result")
    provides("perl-tap-parser-result-bailout")
    provides("perl-tap-parser-result-comment")
    provides("perl-tap-parser-result-plan")
    provides("perl-tap-parser-result-pragma")
    provides("perl-tap-parser-result-test")
    provides("perl-tap-parser-result-unknown")
    provides("perl-tap-parser-result-version")
    provides("perl-tap-parser-result-yaml")
    provides("perl-tap-parser-resultfactory")
    provides("perl-tap-parser-scheduler")
    provides("perl-tap-parser-scheduler-job")
    provides("perl-tap-parser-scheduler-spinner")
    provides("perl-tap-parser-source")
    provides("perl-tap-parser-sourcehandler")
    provides("perl-tap-parser-sourcehandler-executable")
    provides("perl-tap-parser-sourcehandler-file")
    provides("perl-tap-parser-sourcehandler-handle")
    provides("perl-tap-parser-sourcehandler-perl")
    provides("perl-tap-parser-sourcehandler-rawtap")
    provides("perl-tap-parser-yamlish-reader")
    provides("perl-tap-parser-yamlish-writer")
    depends_on("perl-extutils-makemaker", type="build")
