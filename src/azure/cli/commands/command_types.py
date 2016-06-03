from azure.cli.commands import create_command

def cli_command(command_table, name, operation, client_factory=None, return_type=None):
    """ Registers a default Azure CLI command. These commands require no special parameters. """
    command_table[name] = create_command(name, operation, return_type, client_factory)

