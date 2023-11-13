# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import functools

import spack.cmd.common.arguments
import spack.cmd.modules
import spack.config
import spack.modules.ups_version


def add_command(parser, command_dict):
    ups_version_parser = parser.add_parser("ups_version", help="manipulate non-hierarchical module files")
    sp = spack.cmd.modules.setup_parser(ups_version_parser)

    # Set default module file for a package
    setdefault_parser = sp.add_parser(
        "setdefault", help="set the default module file for a package"
    )
    spack.cmd.common.arguments.add_common_arguments(setdefault_parser, ["constraint"])

    callbacks = dict(spack.cmd.modules.callbacks.items())
    callbacks["setdefault"] = setdefault

    command_dict["ups_version"] = functools.partial(
        spack.cmd.modules.modules_cmd, module_type="ups_version", callbacks=callbacks
    )


def setdefault(module_type, specs, args):
    """set the default module file, when multiple are present"""
    # Currently, accepts only a single matching spec
    spack.cmd.modules.one_spec_or_raise(specs)
    spec = specs[0]
    data = {"modules": {args.module_set_name: {"ups_version": {"defaults": [str(spec)]}}}}
    spack.modules.ups_version.configuration_registry = {}
    scope = spack.config.InternalConfigScope("ups_version-setdefault", data)
    with spack.config.override(scope):
        writer = spack.modules.module_types["ups_version"](spec, args.module_set_name)
        writer.update_module_defaults()
