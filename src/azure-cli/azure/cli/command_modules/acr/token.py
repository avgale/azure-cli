# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrestazure.azure_exceptions import CloudError
from azure.cli.core.commands import LongRunningOperation
from azure.cli.core.util import CLIError
from ._utils import get_resource_group_name_by_registry_name, validate_premium_registry, parse_actions_from_repositories

SCOPE_MAPS = 'scopeMaps'
TOKENS = 'tokens'
DEF_SCOPE_MAP_NAME_TEMPLATE = '{}-scope-map'  # append - to minimize incidental collision


def acr_token_create(cmd,
                     client,
                     registry_name,
                     token_name,
                     scope_map_name=None,
                     repository_actions_list=None,
                     status=None,
                     resource_group_name=None,
                     no_passwords=None):
    from knack.log import get_logger
    from ._utils import get_resource_id_by_registry_name

    if bool(repository_actions_list) == bool(scope_map_name):
        raise CLIError("usage error: --repository | --scope-map-name")

    resource_group_name = get_resource_group_name_by_registry_name(cmd.cli_ctx, registry_name, resource_group_name)
    validate_premium_registry(cmd, registry_name, resource_group_name)

    logger = get_logger(__name__)
    if repository_actions_list:
        scope_map_id = _create_default_scope_map(cmd, resource_group_name, registry_name,
                                                 token_name, repository_actions_list, logger)
    else:
        arm_resource_id = get_resource_id_by_registry_name(cmd.cli_ctx, registry_name)
        scope_map_id = '{}/{}/{}'.format(arm_resource_id, SCOPE_MAPS, scope_map_name)

    Token = cmd.get_models('Token')

    poller = client.create(
        resource_group_name,
        registry_name,
        token_name,
        Token(
            scope_map_id=scope_map_id,
            status=status
        )
    )

    if no_passwords:
        return poller

    token = LongRunningOperation(cmd.cli_ctx)(poller)
    _create_default_passwords(cmd, resource_group_name, registry_name, token, logger)
    return token


def _create_default_scope_map(cmd, resource_group_name, registry_name, token_name, repositories, logger):
    from ._client_factory import cf_acr_scope_maps
    scope_map_name = DEF_SCOPE_MAP_NAME_TEMPLATE.format(token_name)
    scope_map_client = cf_acr_scope_maps(cmd.cli_ctx)
    actions = parse_actions_from_repositories(repositories)
    try:
        existing_scope_map = scope_map_client.get(resource_group_name, registry_name, scope_map_name)
        # for command idempotency, if the actions are the same, we accept it
        if sorted(existing_scope_map.actions) == sorted(actions):
            return existing_scope_map.id
        raise CLIError('The default scope map was already configured with different respository permissions.'
                       '\nPlease use "az acr scope-map update -r {} -n {} --add <REPO> --remove <REPO>" to update.'
                       .format(registry_name, scope_map_name))
    except CloudError:
        pass
    logger.warning('Creating a scope map of "%s" for provided respository permissions.', scope_map_name)
    poller = scope_map_client.create(resource_group_name, registry_name, scope_map_name,
                                     actions, "Token {}'s scope map".format(token_name))
    scope_map = LongRunningOperation(cmd.cli_ctx)(poller)
    return scope_map.id


def _create_default_passwords(cmd, resource_group_name, registry_name, token, logger):
    from ._client_factory import cf_acr_token_credentials, cf_acr_registries
    cred_client = cf_acr_token_credentials(cmd.cli_ctx)
    poller = acr_token_credential_generate(cmd, cred_client, registry_name, token.name,
                                           password1=True, password2=True, days=None,
                                           resource_group_name=resource_group_name)
    credentials = LongRunningOperation(cmd.cli_ctx)(poller)
    setattr(token.credentials, 'username', credentials.username)
    setattr(token.credentials, 'passwords', credentials.passwords)
    registry_client = cf_acr_registries(cmd.cli_ctx)
    login_server = registry_client.get(resource_group_name, registry_name).login_server
    logger.warning('Please store your generated credentials safely. Meanwhile you can use it through'
                   ' "docker login %s -u %s -p %s".', login_server, token.credentials.username,
                   token.credentials.passwords[0].value)


def acr_token_delete(cmd,
                     client,
                     registry_name,
                     token_name,
                     yes=None,
                     resource_group_name=None):

    if not yes:
        from knack.prompting import prompt_y_n
        confirmation = prompt_y_n("Deleting the token '{}' will invalidate access to anyone using its credentials. "
                                  "Proceed?".format(token_name))

        if not confirmation:
            return None

    resource_group_name = get_resource_group_name_by_registry_name(cmd.cli_ctx, registry_name, resource_group_name)
    return client.delete(resource_group_name, registry_name, token_name)


def acr_token_update(cmd,
                     client,
                     registry_name,
                     token_name,
                     scope_map_name=None,
                     status=None,
                     resource_group_name=None):

    resource_group_name = get_resource_group_name_by_registry_name(cmd.cli_ctx, registry_name, resource_group_name)

    from ._utils import get_resource_id_by_registry_name

    TokenUpdateParameters = cmd.get_models('TokenUpdateParameters')

    scope_map_id = None
    if scope_map_name:
        arm_resource_id = get_resource_id_by_registry_name(cmd.cli_ctx, registry_name)
        scope_map_id = '{}/{}/{}'.format(arm_resource_id, SCOPE_MAPS, scope_map_name)

    return client.update(
        resource_group_name,
        registry_name,
        token_name,
        TokenUpdateParameters(
            scope_map_id=scope_map_id,
            status=status
        )
    )


def acr_token_show(cmd,
                   client,
                   registry_name,
                   token_name,
                   resource_group_name=None):

    resource_group_name = get_resource_group_name_by_registry_name(cmd.cli_ctx, registry_name, resource_group_name)

    return client.get(
        resource_group_name,
        registry_name,
        token_name
    )


def acr_token_list(cmd,
                   client,
                   registry_name,
                   resource_group_name=None):

    resource_group_name = get_resource_group_name_by_registry_name(cmd.cli_ctx, registry_name, resource_group_name)

    return client.list(
        resource_group_name,
        registry_name
    )


# Credential functions
def acr_token_credential_generate(cmd,
                                  client,
                                  registry_name,
                                  token_name,
                                  password1=False,
                                  password2=False,
                                  days=None,
                                  resource_group_name=None):

    from ._utils import get_resource_id_by_registry_name

    resource_group_name = get_resource_group_name_by_registry_name(cmd.cli_ctx, registry_name, resource_group_name)
    arm_resource_id = get_resource_id_by_registry_name(cmd.cli_ctx, registry_name)
    token_id = '{}/{}/{}'.format(arm_resource_id, TOKENS, token_name)

    # We only want to specify a password if only one was passed.
    name = ("password1" if password1 else "password2") if password1 ^ password2 else None
    expiry = None
    if days:
        from ._utils import add_days_to_now
        expiry = add_days_to_now(days)

    GenerateCredentialsParameters = cmd.get_models('GenerateCredentialsParameters')

    return client.generate_credentials(
        resource_group_name,
        registry_name,
        GenerateCredentialsParameters(
            token_id=token_id,
            name=name,
            expiry=expiry
        )
    )


def acr_token_credential_delete(cmd,
                                client,
                                registry_name,
                                token_name,
                                password1=False,
                                password2=False,
                                resource_group_name=None):

    if not (password1 or password2):
        raise CLIError('No credentials to delete.')

    resource_group_name = get_resource_group_name_by_registry_name(cmd.cli_ctx, registry_name, resource_group_name)

    token = client.get(
        resource_group_name,
        registry_name,
        token_name
    )

    # retrieve the set of existing Token password names. Eg: {'password1', 'password2'}
    password_names = set(map(lambda password: password.name, token.credentials.passwords))

    if password1 and 'password1' not in password_names:
        raise CLIError('Unable to perform operation. Password1 credential doesn\'t exist.')
    if password2 and 'password2' not in password_names:
        raise CLIError('Unable to perform operation. Password2 credential doesn\'t exist.')

    # remove the items which are supposed to be deleted
    if password1:
        password_names.remove('password1')
    if password2:
        password_names.remove('password2')

    TokenPassword = cmd.get_models('TokenPassword')
    new_password_payload = list(map(lambda name: TokenPassword(name=name), password_names))

    TokenUpdateParameters = cmd.get_models('TokenUpdateParameters')
    TokenCredentialsProperties = cmd.get_models('TokenCredentialsProperties')

    return client.update(
        resource_group_name,
        registry_name,
        token_name,
        TokenUpdateParameters(
            credentials=TokenCredentialsProperties(
                passwords=new_password_payload
            )
        )
    )
