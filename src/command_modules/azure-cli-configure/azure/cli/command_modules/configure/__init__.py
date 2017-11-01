# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.sdk.util import CliCommandType

import azure.cli.command_modules.configure._help  # pylint: disable=unused-import


class ConfigureCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        super(ConfigureCommandsLoader, self).__init__(cli_ctx=cli_ctx)
        self.module_name = __name__

    def load_command_table(self, args):
        super(ConfigureCommandsLoader, self).load_command_table(args)

        configure_custom = CliCommandType(operations_tmpl='azure.cli.command_modules.configure.custom#{}')

        with self.command_group('', configure_custom) as g:
            g.command('configure', 'handle_configure')

        return self.command_table

    def load_arguments(self, command):

        super(ConfigureCommandsLoader, self).load_arguments(command)

        with self.argument_context('configure') as c:
            c.argument('defaults', nargs='+', options_list=('--defaults', '-d'))

COMMAND_LOADER_CLS = ConfigureCommandsLoader
