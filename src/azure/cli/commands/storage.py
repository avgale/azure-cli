from msrest import Serializer

from ..main import SESSION
from ..commands import command, description, option
from ._command_creation import get_service_client

@command('storage account list')
@description(_('List storage accounts'))
@option('--resource-group -g <resourceGroup>', _('the resource group name'))
@option('--subscription -s <id>', _('the subscription id'))
def list_accounts(args, unexpected):
    from azure.mgmt.storage import StorageManagementClient, StorageManagementClientConfiguration
    from azure.mgmt.storage.models import StorageAccount
    from msrestazure.azure_active_directory import UserPassCredentials

    smc = get_service_client(StorageManagementClient, StorageManagementClientConfiguration)

    group = args.get('resource-group')
    if group:
        accounts = smc.storage_accounts.list_by_resource_group(group)
    else:
        accounts = smc.storage_accounts.list()

    serializable = Serializer().serialize_data(accounts, "[StorageAccount]")
    return serializable

@command('storage account check')
@option('--account-name <name>')
def checkname(args, unexpected):
    from azure.mgmt.storage import StorageManagementClient, StorageManagementClientConfiguration
    
    smc = get_service_client(StorageManagementClient, StorageManagementClientConfiguration)
    logger.warn(smc.storage_accounts.check_name_availability(args.account_name))
    
    
