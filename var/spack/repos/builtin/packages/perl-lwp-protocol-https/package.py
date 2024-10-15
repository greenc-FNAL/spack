# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlLwpProtocolHttps(PerlPackage):
    """Provide https support for LWP::UserAgent"""

    homepage = "https://metacpan.org/pod/LWP::Protocol::https"
    url = "https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-6.14.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("6.14", sha256="59cdeabf26950d4f1bef70f096b0d77c5b1c5a7b5ad1b66d71b681ba279cbb2a")
    version("6.04", sha256="1ef67750ee363525cf729b59afde805ac4dc80eaf8d36ca01082a4d78a7af629")
    version("6.03", sha256="cb864de7677cc3fc9f8f4aaa17c2984d970fdfa46fc7e3cb90bc5ef2c3e3c6f1")

    provides("perl-lwp-protocol-https-socket")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-net-https@6:", type="run")
    depends_on("perl-lwp-useragent@6.6:", type=("build", "run", "test"))
    depends_on("perl-mozilla-ca@20180117:", type="run")
    depends_on("perl@5.8.1:", type=("build", "run", "test"))
    depends_on("perl-io-socket-ssl-utils", type=("build", "test"))
    depends_on("perl-io-socket-ssl@1.54:", type=("build", "run", "test"))
    depends_on("perl-test-requiresinternet", type=("build", "test"))
    depends_on("perl-lwp-protocol-http", type="run")

    def url_for_version(self, version):
        if self.spec.satisfies("@6.07:"):
            return f"https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-{version}.tar.gz"
        else:
            return f"http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/LWP-Protocol-https-{version}.tar.gz"
