# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlHtmlForm(PerlPackage):
    """Class that represents an HTML form element."""

    homepage = "https://github.com/libwww-perl/HTML-Form"
    url = "https://cpan.metacpan.org/authors/id/S/SI/SIMBABQUE/HTML-Form-6.10.tar.gz"

    license("Artistic-1.0-Perl OR GPL-1.0-or-later", checked_by="greenc-FNAL")

    maintainers("gartung", "greenc-FNAL", "marcmengel")

    version("6.10", sha256="df8393e35e495a0839f06a63fb65d6922842c180d260554137728a9f092df9d3")
    version("6.09", sha256="f6c06ce1e54f9cfe1fd800d886126b875c972716a27fc281d3fb00345132e230")

    provides("perl-html-form-fileinput")
    provides("perl-html-form-ignoreinput")
    provides("perl-html-form-imageinput")
    provides("perl-html-form-input")
    provides("perl-html-form-keygeninput")
    provides("perl-html-form-listinput")
    provides("perl-html-form-submitinput")
    provides("perl-html-form-textinput")
    depends_on("perl-http-response", type=("build", "test"))
    depends_on("perl@5.8.1:", type="run")
    depends_on("perl-uri@1.10:", type="run")
    depends_on("perl-html-tokeparser", type="run")
    depends_on("perl-http-request-common@6.3:", type="run")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-http-request@6:", type="run")
