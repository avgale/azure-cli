# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType
from azure.cli.core.profiles import ResourceType


def load_command_table(self, _):
    from azure.cli.command_modules.eventhubs._client_factory import (event_hub_mgmt_client_factory,
                                                                     schema_registry_mgmt_client_factory,
                                                                     application_group_mgmt_client_factory)

    eh_namespace_custom = CliCommandType(
        operations_tmpl='azure.cli.command_modules.eventhubs.operations.namespace_custom#{}',
    )

    eh_network_custom = CliCommandType(
        operations_tmpl='azure.cli.command_modules.eventhubs.operations.network_rule_set#{}'
    )

    eh_event_hub_util = CliCommandType(
        operations_tmpl='azure.mgmt.eventhub.operations#EventHubsOperations.{}',
        client_factory=event_hub_mgmt_client_factory,
        resource_type=ResourceType.MGMT_EVENTHUB)

    eh_application_group_util = CliCommandType(
        operations_tmpl='azure.mgmt.eventhub.operations#ApplicationGroupOperations.{}',
        client_factory=schema_registry_mgmt_client_factory,
        resource_type=ResourceType.MGMT_EVENTHUB
    )

# Namespace Region
    with self.command_group('eventhubs namespace', custom_command_type=eh_namespace_custom,
                            is_preview=True) as g:
        g.custom_command('create', 'create_eventhub_namespace')

    with self.command_group('eventhubs namespace private-endpoint-connection', custom_command_type=eh_namespace_custom,
                            is_preview=True) as g:
        from ._validator import validate_private_endpoint_connection_id
        g.custom_command('approve', 'approve_private_endpoint_connection', validator=validate_private_endpoint_connection_id)
        g.custom_command('reject', 'reject_private_endpoint_connection', validator=validate_private_endpoint_connection_id)
        g.custom_command('delete', 'delete_private_endpoint_connection', confirmation=True, validator=validate_private_endpoint_connection_id)

# EventHub Region
    with self.command_group('eventhubs eventhub', eh_event_hub_util, resource_type=ResourceType.MGMT_EVENTHUB, client_factory=event_hub_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_eheventhub_create')
        g.show_command('show', 'get')
        g.command('list', 'list_by_namespace')
        g.command('delete', 'delete')
        g.generic_update_command('update', custom_func_name='cli_eheventhub_update')

# DisasterRecoveryConfigs Region
    with self.command_group('eventhubs georecovery-alias', custom_command_type=eh_namespace_custom,
                            is_preview=True) as g:
        g.custom_command('set', 'set_georecovery_alias', supports_no_wait=True)

# NetworkRuleSet Region
    with self.command_group('eventhubs namespace network-rule-set ip-rule', custom_command_type=eh_network_custom,
                            is_preview=True) as g:
        g.custom_command('add', 'add_network_rule_set_ip_rule')
        g.custom_command('remove', 'remove_network_rule_set_ip_rule')

    with self.command_group('eventhubs namespace network-rule-set virtual-network-rule', custom_command_type=eh_network_custom,
                            is_preview=True) as g:
        g.custom_command('add', 'add_virtual_network_rule')
        g.custom_command('remove', 'remove_virtual_network_rule')

# Identity Region
    with self.command_group('eventhubs namespace identity', custom_command_type=eh_namespace_custom,
                            is_preview=True) as g:
        g.custom_command('assign', 'cli_add_identity')
        g.custom_command('remove', 'cli_remove_identity')

# Encryption Region
    with self.command_group('eventhubs namespace encryption', custom_command_type=eh_namespace_custom,
                            is_preview=True) as g:
        g.custom_command('add', 'cli_add_encryption')
        g.custom_command('remove', 'cli_remove_encryption')

# ApplicationGroup Region
    with self.command_group('eventhubs namespace application-group', eh_application_group_util, resource_type=ResourceType.MGMT_EVENTHUB, client_factory=application_group_mgmt_client_factory) as g:
        g.custom_command('create', 'cli_appgroup_create')
        g.custom_command('update', 'cli_appgroup_update')
        g.show_command('show', 'get')
        g.command('delete', 'delete')
        g.command('list', 'list_by_namespace')

    with self.command_group('eventhubs namespace application-group policy', eh_application_group_util, resource_type=ResourceType.MGMT_EVENTHUB, client_factory=application_group_mgmt_client_factory) as g:
        g.custom_command('add', 'cli_add_appgroup_policy')
        g.custom_command('remove', 'cli_remove_appgroup_policy')
