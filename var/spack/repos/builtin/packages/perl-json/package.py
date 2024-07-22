# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlJson(PerlPackage):
    """JSON (JavaScript Object Notation) encoder/decoder"""

    homepage = "https://metacpan.org/pod/JSON"
    url = "https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/JSON-4.09.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("4.10", sha256="df8b5143d9a7de99c47b55f1a170bd1f69f711935c186a6dc0ab56dd05758e35")
    version("4.09", sha256="6780a51f438c0932eec0534fc9cd2b1ad0d64817eda4add8ede5ec77d6d2c991")
    version("4.08", sha256="6b2a38eb6f92934840d142e31ce6683610b66477fad3ffab1111978ef26ca53f")
    version("2.97001", sha256="e277d9385633574923f48c297e1b8acad3170c69fa590e31fa466040fc6f8f5a")

    variant(
        "json-xs",
        default=True,
        description="""Makes the preferred backend JSON::XS available to avoid defaulting to the
        slower JSON::PP""",
    )

    provides("perl-json-backend-pp")

    depends_on("perl-extutils-makemaker", type="build")

    depends_on("perl-json-xs@2.34:", when="+json-xs", type=("run"))
