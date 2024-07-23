# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import inspect

from spack.package import *


class PerlNetSsleay(PerlPackage):
    """Perl extension for using OpenSSL"""

    homepage = "https://metacpan.org/pod/Net::SSLeay"
    url = "https://cpan.metacpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-1.92.tar.gz"

    license("Artistic-2.0")

    version("1.93_01", sha256="876d022fbc719631b11d6bb4b6e78db3c19bbca578093c376c8f9900a4432aa3")
    version(
        "1.92",
        sha256="47c2f2b300f2e7162d71d699f633dd6a35b0625a00cbda8c50ac01144a9396a9",
        preferred=True,
    )
    version("1.90", sha256="f8696cfaca98234679efeedc288a9398fcf77176f1f515dbc589ada7c650dc93")
    version(
        "1.85",
        sha256="9d8188b9fb1cae3bd791979c20554925d5e94a138d00414f1a6814549927b0c8",
        url="https://cpan.metacpan.org/authors/id/M/MI/MIKEM/Net-SSLeay-1.82.tar.gz",
    )
    version(
        "1.84",
        sha256="823ec3cbb428309d6a9e56f362a9300693ce3215b7fede109adb7be361fff177",
        url="https://cpan.metacpan.org/authors/id/M/MI/MIKEM/Net-SSLeay-1.82.tar.gz",
    )
    version(
        "1.83",
        sha256="c45857c829a48ebf9ecc46e904d20827ad38dde0eb8d5e8b47895260ae6827b7",
        url="https://cpan.metacpan.org/authors/id/M/MI/MIKEM/Net-SSLeay-1.82.tar.gz",
    )
    version(
        "1.82",
        sha256="5895c519c9986a5e5af88e3b8884bbdc70e709ee829dc6abb9f53155c347c7e5",
        url="https://cpan.metacpan.org/authors/id/M/MI/MIKEM/Net-SSLeay-1.82.tar.gz",
    )

    depends_on("c", type="build")  # generated

    depends_on("openssl")

    provides("perl-net-ssleay-handle")
    depends_on("perl@5.8.1:", type="run")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-scalar-util", type=("build", "test"))


class PerlBuilder(spack.build_systems.perl.PerlBuilder):
    class _WrappedExecutable(Executable):
        def __init__(self, executable):
            super(PerlBuilder._WrappedExecutable, self).__init__(executable.path)

        def __call__(self, *args, **kwargs):
            # Do you want to run external tests?
            config_answers = ["\n"]
            config_answers_filename = "spack-config.in"

            with open(config_answers_filename, "w") as f:
                f.writelines(config_answers)

            with open(config_answers_filename, "r") as f:
                super(PerlBuilder._WrappedExecutable, self).__call__(*args, **kwargs, input=f)

    def configure(self, pkg, spec, prefix):
        env["OPENSSL_PREFIX"] = self.spec["openssl"].prefix
        perl_safe = inspect.getmodule(self).perl
        inspect.getmodule(self).perl = PerlBuilder._WrappedExecutable(perl_safe)

        try:
            super(PerlBuilder, self).configure(pkg, spec, prefix)
        finally:
            inspect.getmodule(self).perl = perl_safe
