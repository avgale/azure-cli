﻿from __future__ import print_function
from datetime import datetime
from os import environ
from sys import stderr
from six.moves import input # pylint: disable=redefined-builtin

from azure.storage.blob import PublicAccess, BlockBlobService
from azure.mgmt.storage import StorageManagementClient, StorageManagementClientConfiguration
from azure.mgmt.storage.models import AccountType
from azure.mgmt.storage.operations import StorageAccountsOperations

from azure.cli.parser import IncorrectUsageError

from ..commands import (CommandTable, AutoCommandDefinition,
                        COMMON_PARAMETERS as GLOBAL_COMMON_PARAMETERS)
from ._command_creation import get_mgmt_service_client, get_data_service_client
from ..commands._auto_command import build_operation
from .._locale import L

command_table = CommandTable()

def extend_parameter(parameter_metadata, **kwargs):
    modified_parameter_metadata = parameter_metadata.copy()
    modified_parameter_metadata.update(kwargs)
    return modified_parameter_metadata

COMMON_PARAMETERS = GLOBAL_COMMON_PARAMETERS.copy()
COMMON_PARAMETERS.update({
    'account-key': {
        'name': '--account-key -k',
        'help': L('the storage account key'),
        # While account key *may* actually be required if the environment variable hasn't been
        # specified, it is only required unless the connection string has been specified
        'required': False,
        'default': environ.get('AZURE_STORAGE_ACCESS_KEY')
    },
    'account-name': {
        'name': '--account-name -n',
        'help': L('the storage account name'),
        # While account name *may* actually be required if the environment variable hasn't been
        # specified, it is only required unless the connection string has been specified
        'required': False,
        'default': environ.get('AZURE_STORAGE_ACCOUNT')
    },
    'blob-name': {
        'name': '--blob-name -b',
        'help': L('the name of the blob'),
        'required': True
    },
    'container-name': {
        'name': '--container-name -c',
        'required': True
    },
    'connection-string': {
        'name': '--connection-string',
        'help': L('the storage connection string'),
        # You can either specify connection string or name/key. There is no convenient way
        # to express this kind of relationship in argparse...
        # TODO: Move to exclusive group
        'required': False,
        'default': environ.get('AZURE_STORAGE_CONNECTION_STRING')
    },
    'if-modified-since': {
        'name': '--if-modified-since',
        'help': L('alter only if modified since supplied UTC datetime'),
        'required': False,
    },
    'if-unmodified-since': {
        'name': '--if-unmodified-since',
        'help': L('alter only if unmodified since supplied UTC datetime'),
        'required': False,
    },
    'optional-resource-group-name':
        extend_parameter(GLOBAL_COMMON_PARAMETERS['resource-group-name'], required=False),
    'share-name': {
        'name': '--share-name',
        'help': L('the name of the file share'),
        'required': True,
    },
    'timeout': {
        'name': '--timeout',
        'help': L('timeout in seconds'),
        'required': False,
    }
})

def _storage_client_factory(*args): # pylint: disable=unused-argument
    return get_mgmt_service_client(StorageManagementClient, StorageManagementClientConfiguration)

def _blob_data_service_factory(*args):
    def _resolve_arg(key, envkey):
        try:
            value = args[0][key]
            args[0].pop(key, None)
        except (IndexError, KeyError):
            value = environ.get(envkey)
        return value

    return get_data_service_client(
        BlockBlobService,
        _resolve_arg('account-name', 'AZURE_STORAGE_ACCOUNT'),
        _resolve_arg('account-key', 'AZURE_STORAGE_ACCOUNT_KEY'),
        _resolve_arg('connection-string', 'AZURE_STORAGE_CONNECTION_STRING'))

# ACCOUNT COMMANDS

build_operation(
    'storage account',
    'storage_accounts',
    _storage_client_factory,
    [
        AutoCommandDefinition(StorageAccountsOperations.check_name_availability,
                              'Result', 'check-name'),
        AutoCommandDefinition(StorageAccountsOperations.delete, None),
        AutoCommandDefinition(StorageAccountsOperations.get_properties, 'StorageAccount', 'show'),
        AutoCommandDefinition(StorageAccountsOperations.list_keys, '[StorageAccountKeys]')
    ],
    command_table)

@command_table.command('storage account list', description=L('List storage accounts.'))
@command_table.option(**COMMON_PARAMETERS['optional-resource-group-name'])
def list_accounts(args):
    from azure.mgmt.storage.models import StorageAccount
    from msrestazure.azure_active_directory import UserPassCredentials
    smc = _storage_client_factory()
    group = args.get('resource-group-name')
    if group:
        accounts = smc.storage_accounts.list_by_resource_group(group)
    else:
        accounts = smc.storage_accounts.list()
    return list(accounts)

@command_table.command('storage account renew-keys')
@command_table.description(L('Regenerate one or both keys for a storage account.'))
@command_table.option(**COMMON_PARAMETERS['resource-group-name'])
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option('--key -y', default=['key1', 'key2'],
                      choices=['key1', 'key2'], help=L('Key to renew'))
def renew_account_keys(args):
    smc = _storage_client_factory()
    for key in args.get('key'):
        result = smc.storage_accounts.regenerate_key(
            resource_group_name=args.get('resource-group-name'),
            account_name=args.get('account-name'),
            key_name=key)
    return result

@command_table.command('storage account usage')
@command_table.description(
    L('Show the current count and limit of the storage accounts under the subscription.'))
def show_account_usage(_):
    smc = _storage_client_factory()
    return next((x for x in smc.usage.list() if x.name.value == 'StorageAccounts'), None)

@command_table.command('storage account connection-string')
@command_table.description(L('Show the connection string for a storage account.'))
@command_table.option(**COMMON_PARAMETERS['resource-group-name'])
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option('--use-http', action='store_const', const='http', default='https',
                      help=L('use http as the default endpoint protocol'))
def show_storage_connection_string(args):
    smc = _storage_client_factory()

    endpoint_protocol = args.get('use-http')
    storage_account = args.get('account-name')
    keys = smc.storage_accounts.list_keys(args.get('resource-group-name'), storage_account)

    connection_string = 'DefaultEndpointsProtocol={};AccountName={};AccountKey={}'.format(
        endpoint_protocol,
        storage_account,
        keys.key1) #pylint: disable=no-member
    return {'ConnectionString':connection_string}

# TODO: update this once enums are supported in commands first-class (task #115175885)
storage_account_types = {'Standard_LRS': AccountType.standard_lrs,
                         'Standard_ZRS': AccountType.standard_zrs,
                         'Standard_GRS': AccountType.standard_grs,
                         'Standard_RAGRS': AccountType.standard_ragrs,
                         'Premium_LRS': AccountType.premium_lrs}
storage_account_type_string = ' | '.join(storage_account_types)

@command_table.command('storage account create')
@command_table.description(L('Create a storage account.'))
@command_table.option(**COMMON_PARAMETERS['resource-group-name'])
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['location'])
@command_table.option('--type',
                      help=L('Values: {}'.format(storage_account_type_string)),
                      choices=storage_account_types.keys(),
                      type=lambda x: storage_account_types[x],
                      required=True)
@command_table.option('--tags',
                      help=L('storage account tags. Tags are key=value pairs separated ' + \
                      'with a semicolon(;)'))
def create_account(args):
    from azure.mgmt.storage.models import StorageAccountCreateParameters
    smc = _storage_client_factory()

    resource_group = args.get('resource-group')
    account_name = args.get('account-name')
    try:
        account_type = storage_account_types[args.get('type')]
    except KeyError:
        raise IncorrectUsageError(L('type must be: {}'
                                    .format(storage_account_type_string)))
    params = StorageAccountCreateParameters(args.get('location'),
                                            account_type,
                                            _parse_dict(args, 'tags'))
    return smc.storage_accounts.create(resource_group, account_name, params)

@command_table.command('storage account set')
@command_table.description(L('Update storage account property (only one at a time).'))
@command_table.option(**COMMON_PARAMETERS['resource-group-name'])
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option('--type',
                      help=L('Values: {}'.format(storage_account_type_string)),
                      choices=storage_account_types.keys(),
                      type=lambda x: storage_account_types[x])
@command_table.option('--tags',
                      help=L('storage account tags. Tags are key=value pairs separated ' + \
                      'with a semicolon(;)'))
@command_table.option('--custom-domain', help=L('the custom domain name'))
@command_table.option('--subdomain', help=L('use indirect CNAME validation'))
def set_account(args):
    from azure.mgmt.storage.models import StorageAccountUpdateParameters, CustomDomain
    smc = _storage_client_factory()

    resource_group = args.get('resource-group')
    account_name = args.get('account-name')
    domain = args.get('custom-domain')
    try:
        account_type = storage_account_types[args.get('type')] if args.get('type') else None
    except KeyError:
        raise IncorrectUsageError(L('type must be: {}'
                                    .format(storage_account_type_string)))
    params = StorageAccountUpdateParameters(_parse_dict(args, 'tags'), account_type, domain)
    return smc.storage_accounts.update(resource_group, account_name, params)

# CONTAINER COMMANDS

build_operation(
    'storage container', None, _blob_data_service_factory,
    [
        AutoCommandDefinition(BlockBlobService.list_containers, '[Container]', 'list'),
        AutoCommandDefinition(BlockBlobService.delete_container, 'None', 'delete'),
        AutoCommandDefinition(BlockBlobService.get_container_properties,
                              '[ContainerProperties]', 'show'),
        AutoCommandDefinition(BlockBlobService.create_container, 'None', 'create')
    ],
    command_table)
    #extra_args=STORAGE_DATA_CLIENT_ARGS)

# TODO: update this once enums are supported in commands first-class (task #115175885)
public_access_types = {'none': None,
                       'blob': PublicAccess.Blob,
                       'container': PublicAccess.Container}
public_access_string = ' | '.join(public_access_types)

@command_table.command('storage container create')
@command_table.description(L('Create a storage container.'))
@command_table.option(**COMMON_PARAMETERS['container-name'])
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
@command_table.option('--public-access', default=None, choices=public_access_types.keys(),
                      type=lambda x: public_access_types[x],
                      help=L('Values: {}'.format(public_access_string)))
@command_table.option('--metadata', help=L('dict of key=value pairs (separated by ;)'))
@command_table.option('--fail-on-exist',
                      help=L('operation fails if container already exists'), action='store_true')
@command_table.option(**COMMON_PARAMETERS['timeout'])
def create_container(args):
    bbs = _blob_data_service_factory(args)
    public_access = args.get('public-access')
    metadata = _parse_dict(args, 'metadata', allow_singles=False)
    if not bbs.create_container(
            container_name=args.get('container-name'),
            public_access=public_access,
            metadata=metadata,
            fail_on_exist=args.get('fail-on-exist'),
            timeout=_parse_int(args, 'timeout')):
        raise RuntimeError(L('Container creation failed.'))

@command_table.command('storage container delete')
@command_table.description(L('Delete a storage container.'))
@command_table.option(**COMMON_PARAMETERS['container-name'])
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
@command_table.option('--force -f', help=L('supress delete confirmation prompt'))
@command_table.option('--fail-not-exist', help=L('operation fails if container does not exist'))
@command_table.option('--lease-id', help=L('delete only if lease is ID active and matches'))
@command_table.option(**COMMON_PARAMETERS['if-modified-since'])
@command_table.option(**COMMON_PARAMETERS['if-unmodified-since'])
@command_table.option(**COMMON_PARAMETERS['timeout'])
def delete_container(args):
    bbs = _blob_data_service_factory(args)
    container_name = args.get('container-name')

    if args.get('force') is None:
        ans = input('Really delete {}? [Y/n] '.format(container_name))
        if not ans or ans[0].lower() != 'y':
            return 0

    if not bbs.delete_container(
            container_name=container_name,
            fail_not_exist=True if args.get('fail-not-exist') else False,
            lease_id=args.get('lease-id'),
            if_unmodified_since=_parse_datetime(args, 'if-unmodified-since'),
            if_modified_since=_parse_datetime(args, 'if-modified-since'),
            timeout=_parse_int(args, 'timeout')):
        raise RuntimeError(L('Container deletion failed.'))

@command_table.command('storage container exists')
@command_table.description(L('Check if a storage container exists.'))
@command_table.option(**COMMON_PARAMETERS['container-name'])
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
@command_table.option('--snapshot',
                      help=L('UTC datetime value which specifies a snapshot'))
@command_table.option(**COMMON_PARAMETERS['timeout'])
def exists_container(args):
    bbs = _blob_data_service_factory(args)
    return str(bbs.exists(
        container_name=args.get('container-name'),
        snapshot=_parse_datetime(args, 'snapshot'),
        timeout=_parse_int(args, 'timeout')))


lease_duration_values = {'min':15, 'max':60, 'infinite':-1}
lease_duration_values_string = 'Between {} and {} seconds. ({} for infinite)'.format(
    lease_duration_values['min'],
    lease_duration_values['max'],
    lease_duration_values['infinite'])

build_operation('storage container lease', None, _blob_data_service_factory,
                [
                    AutoCommandDefinition(BlockBlobService.renew_container_lease, 'None', 'renew'),
                    AutoCommandDefinition(BlockBlobService.release_container_lease,
                                          'None', 'release'),
                    AutoCommandDefinition(BlockBlobService.change_container_lease,
                                          'LeaseId', 'change')
                ],
                command_table)
                #extra_args=STORAGE_DATA_CLIENT_ARGS)

@command_table.command('storage container lease acquire')
@command_table.description(L('Acquire a lock on a container for delete operations.'))
@command_table.option(**COMMON_PARAMETERS['container-name'])
@command_table.option('--lease-duration',
                      help=L('Values: {}'.format(lease_duration_values_string)),
                      required=True)
@command_table.option('--proposed-lease-id', help=L('proposed lease id in GUID format'))
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
@command_table.option(**COMMON_PARAMETERS['if-modified-since'])
@command_table.option(**COMMON_PARAMETERS['if-unmodified-since'])
@command_table.option(**COMMON_PARAMETERS['timeout'])
def acquire_container_lease(args):
    bbs = _blob_data_service_factory(args)
    try:
        lease_duration = int(args.get('lease-duration'))
    except ValueError:
        raise IncorrectUsageError('lease-duration must be: {}'.format(lease_duration_values_string))

    return bbs.acquire_container_lease(
        container_name=args.get('container-name'),
        lease_duration=lease_duration,
        proposed_lease_id=args.get('proposed-lease-id'),
        if_modified_since=_parse_int(args, 'if-modified-since'),
        if_unmodified_since=_parse_int(args, 'if-unmodified-since'),
        timeout=True if args.get('timeout') else False)

@command_table.command('storage container lease break')
@command_table.description(L('Break a lock on a container for delete operations.'))
@command_table.option(**COMMON_PARAMETERS['container-name'])
@command_table.option('--lease-break-period',
                      help=L('Values: {}'.format(lease_duration_values_string)), required=True)
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
@command_table.option(**COMMON_PARAMETERS['if-modified-since'])
@command_table.option(**COMMON_PARAMETERS['if-unmodified-since'])
@command_table.option(**COMMON_PARAMETERS['timeout'])
def break_container_lease(args):
    bbs = _blob_data_service_factory(args)
    try:
        lease_break_period = int(args.get('lease-break-period'))
    except ValueError:
        raise ValueError('lease-break-period must be: {}'.format(lease_duration_values_string))
    bbs.break_container_lease(
        container_name=args.get('container-name'),
        lease_break_period=lease_break_period,
        if_modified_since=_parse_int(args, 'if-modified-since'),
        if_unmodified_since=_parse_int(args, 'if-unmodified-since'),
        timeout=True if args.get('timeout') else False)

# BLOB COMMANDS

build_operation('storage blob', None, _blob_data_service_factory,
                [
                    AutoCommandDefinition(BlockBlobService.list_blobs, '[Blob]', 'list'),
                    AutoCommandDefinition(BlockBlobService.delete_blob, 'None', 'delete'),
                    AutoCommandDefinition(BlockBlobService.exists, 'Boolean', 'exists'),
                    AutoCommandDefinition(BlockBlobService.get_blob_properties,
                                          'BlobProperties', 'show')
                ],
                command_table)
                #extra_args=STORAGE_DATA_CLIENT_ARGS)

@command_table.command('storage blob upload-block-blob')
@command_table.description(L('Upload a block blob to a container.'))
@command_table.option(**COMMON_PARAMETERS['container-name'])
@command_table.option(**COMMON_PARAMETERS['blob-name'])
@command_table.option('--upload-from', required=True)
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
@command_table.option('--container.public-access', default=None,
                      choices=public_access_types.keys(),
                      type=lambda x: public_access_types[x])
@command_table.option('--content.type')
@command_table.option('--content.disposition')
@command_table.option('--content.encoding')
@command_table.option('--content.language')
@command_table.option('--content.md5')
@command_table.option('--content.cache-control')
def create_block_blob(args):
    from azure.storage.blob import ContentSettings
    bbs = _blob_data_service_factory(args)
    try:
        public_access = public_access_types[args.get('public-access')] \
                                            if args.get('public-access') \
                                            else None
    except KeyError:
        raise IncorrectUsageError(L('container.public-access must be: {}'
                                    .format(public_access_string)))

    bbs.create_container(args.get('container-name'), public_access=public_access)

    return bbs.create_blob_from_path(
        container_name=args.get('container-name'),
        blob_name=args.get('blob-name'),
        file_path=args.get('upload-from'),
        progress_callback=_update_progress,
        content_settings=ContentSettings(content_type=args.get('content.type'),
                                         content_disposition=args.get('content.disposition'),
                                         content_encoding=args.get('content.encoding'),
                                         content_language=args.get('content.language'),
                                         content_md5=args.get('content.md5'),
                                         cache_control=args.get('content.cache-control'))
        )

@command_table.command('storage blob download')
@command_table.description(L('Download the specified blob.'))
@command_table.option(**COMMON_PARAMETERS['container-name'])
@command_table.option(**COMMON_PARAMETERS['blob-name'])
@command_table.option('--download-to', help=L('the file path to download to'), required=True)
def download_blob(args):
    bbs = _blob_data_service_factory(args)

    # show dot indicator of download progress (one for every 10%)
    bbs.get_blob_to_path(args.get('container-name'),
                         args.get('blob-name'),
                         args.get('download-to'),
                         progress_callback=_update_progress)

# SHARE COMMANDS

@command_table.command('storage share exists')
@command_table.description(L('Check if a file share exists.'))
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
def exist_share(args):
    fsc = _get_file_service_client(args)
    return str(fsc.exists(share_name=args.get('share-name')))

@command_table.command('storage share list')
@command_table.description(L('List file shares within a storage account.'))
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
@command_table.option('--prefix -p', help=L('share name prefix to filter by'))
def list_shares(args):
    fsc = _get_file_service_client(args)
    return list(fsc.list_shares(prefix=args.get('prefix')))

@command_table.command('storage share contents')
@command_table.description(L('List files and directories inside a share path.'))
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option('--directory-name -d', help=L('share subdirectory path to examine'))
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
def list_files(args):
    fsc = _get_file_service_client(args)
    return list(fsc.list_directories_and_files(
        args.get('share-name'),
        directory_name=args.get('directory-name')))

@command_table.command('storage share create')
@command_table.description(L('Create a new file share.'))
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
def create_share(args):
    fsc = _get_file_service_client(args)
    if not fsc.create_share(args.get('share-name')):
        raise RuntimeError(L('Share creation failed.'))

@command_table.command('storage share delete')
@command_table.description(L('Create a new file share.'))
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
def delete_share(args):
    fsc = _get_file_service_client(args)
    if not fsc.delete_share(args.get('share-name')):
        raise RuntimeError(L('Share deletion failed.'))

# DIRECTORY COMMANDS

@command_table.command('storage directory exists')
@command_table.description(L('Check if a directory exists.'))
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option('--directory-name -d', help=L('the directory name'), required=True)
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
def exist_directory(args):
    fsc = _get_file_service_client(args)
    return str(fsc.exists(share_name=args.get('share-name'),
                          directory_name=args.get('directory-name')))

@command_table.command('storage directory create')
@command_table.description(L('Create a directory within a share.'))
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option('--directory-name -d', help=L('the directory to create'), required=True)
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
def create_directory(args):
    fsc = _get_file_service_client(args)
    if not fsc.create_directory(
            share_name=args.get('share-name'),
            directory_name=args.get('directory-name')):
        raise RuntimeError(L('Directory creation failed.'))

@command_table.command('storage directory delete')
@command_table.description(L('Delete a directory within a share.'))
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option('--directory-name -d', help=L('the directory to delete'), required=True)
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
def delete_directory(args):
    fsc = _get_file_service_client(args)
    if not fsc.delete_directory(
            share_name=args.get('share-name'),
            directory_name=args.get('directory-name')):
        raise RuntimeError(L('Directory deletion failed.'))

# FILE COMMANDS

@command_table.command('storage file download')
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option('--file-name -f', help=L('the file name'), required=True)
@command_table.option('--local-file-name', help=L('the path to the local file'), required=True)
@command_table.option('--directory-name -d', help=L('the directory name'))
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
def storage_file_download(args):
    fsc = _get_file_service_client(args)
    fsc.get_file_to_path(args.get('share-name'),
                         args.get('directory-name'),
                         args.get('file-name'),
                         args.get('local-file-name'),
                         progress_callback=_update_progress)

@command_table.command('storage file exists')
@command_table.description(L('Check if a file exists.'))
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option('--file-name -f', help=L('the file name to check'), required=True)
@command_table.option('--directory-name -d', help=L('subdirectory path to the file'))
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
def exist_file(args):
    fsc = _get_file_service_client(args)
    return str(fsc.exists(share_name=args.get('share-name'),
                          directory_name=args.get('directory-name'),
                          file_name=args.get('file-name')))

@command_table.command('storage file upload')
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option('--file-name -f', help=L('the destination file name'), required=True)
@command_table.option('--local-file-name', help=L('the file name to upload'), required=True)
@command_table.option('--directory-name -d', help=L('the destination directory to upload to'))
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['container-name'])
def storage_file_upload(args):
    fsc = _get_file_service_client(args)
    fsc.create_file_from_path(args.get('share-name'),
                              args.get('directory-name'),
                              args.get('file-name'),
                              args.get('local-file-name'),
                              progress_callback=_update_progress)

@command_table.command('storage file delete')
@command_table.option(**COMMON_PARAMETERS['share-name'])
@command_table.option('--file-name -f', help=L('the file name to delete'), required=True)
@command_table.option('--directory-name -d', help=L('the directory name'))
@command_table.option(**COMMON_PARAMETERS['account-name'])
@command_table.option(**COMMON_PARAMETERS['account-key'])
@command_table.option(**COMMON_PARAMETERS['connection-string'])
def storage_file_delete(args):
    fsc = _get_file_service_client(args)
    fsc.delete_file(args.get('share-name'),
                    args.get('directory-name'),
                    args.get('file-name'))

# HELPER METHODS

def _get_file_service_client(args):
    from azure.storage.file import FileService
    return get_data_service_client(FileService,
                                   _resolve_storage_account(args),
                                   _resolve_storage_account_key(args),
                                   _resolve_connection_string(args))

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def _parse_datetime(args, key):
    # TODO This should handle timezone
    datestring = args.get(key)
    if not datestring:
        return None
    time = datetime.strptime(datestring, DATETIME_FORMAT)
    return time

def _parse_dict(args, key, allow_singles=True):
    """ Parses dictionaries passed in as argument strings in key=value;key=value format.
    If 'allow_singles' is set to False, single tags will be ignored."""
    string_val = args.get(key)
    if not string_val:
        return None
    kv_list = [x for x in string_val.split(';') if '=' in x]     # key-value pairs
    result = dict(x.split('=') for x in kv_list)
    if allow_singles:
        s_list = [x for x in string_val.split(';') if '=' not in x]  # single values
        result.update(dict((x, '') for x in s_list))
    return result

def _parse_int(args, key):
    try:
        str_val = args.get(key)
        int_val = int(str_val) if str_val else None
    except ValueError:
        int_val = None
    return int_val

# TODO: Remove once these parameters are supported first-class by @option (task #116054675)
def _resolve_storage_account(args):
    return args.get('account-name') or environ.get('AZURE_STORAGE_ACCOUNT')

def _resolve_storage_account_key(args):
    return args.get('account-key') or environ.get('AZURE_STORAGE_ACCESS_KEY')

def _resolve_connection_string(args):
    return args.get('connection-string') or environ.get('AZURE_STORAGE_CONNECTION_STRING')

def _update_progress(current, total):
    if total:
        message = 'Percent complete: %'
        num_format = 'xxx.x'
        num_decimals = len(num_format.split('.', maxsplit=1)[1]) if '.' in num_format else 0
        format_string = '{:.%sf}' % num_decimals
        percent_done = format_string.format(current * 100 / total)
        padding = len(num_format) - len(percent_done)
        message += (' ' * padding) + percent_done
        print('\b' * len(message) + message, end='', file=stderr, flush=True)
