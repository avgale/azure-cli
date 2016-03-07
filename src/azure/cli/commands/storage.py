﻿from msrest import Serializer
from ..commands import command, description, option
from ._command_creation import get_service_client
from .._argparse import IncorrectUsageError
from .._logging  import logger
from .._locale import L

@command('storage account list')
@description(L('List storage accounts'))
@option('--resource-group -g <resourceGroup>', L('the resource group name'))
@option('--subscription -s <id>', L('the subscription id'))
def list_accounts(args, unexpected): #pylint: disable=unused-argument
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
@option('--account-name -an <name>')
def checkname(args, unexpected): #pylint: disable=unused-argument
    from azure.mgmt.storage import StorageManagementClient, StorageManagementClientConfiguration
    smc = get_service_client(StorageManagementClient, StorageManagementClientConfiguration)
    logger.warning(smc.storage_accounts.check_name_availability(args.account_name))

@command('storage blob blockblob create')
@option('--account-name -an <name>', required=True)
@option('--account-key -ak <key>', required=True)
@option('--container -c <name>', required=True)
@option('--blob-name -bn <name>', required=True)
@option('--upload-from -uf <file>', required=True)
@option('--container.public-access -cpa <none, blob, container>')
@option('--content-settings.type -cst <type>')
@option('--content-settings.disposition -csd <setting>')
@option('--content-settings.encoding -cse <setting>')
@option('--content-settings.language -csl <setting>')
@option('--content-settings.md5 -csm <setting>')
@option('--content-settings.cache-control -cscc <setting>')
def create_block_blob(args, unexpected): #pylint: disable=unused-argument
    from azure.storage.blob import BlockBlobService, PublicAccess, ContentSettings

    block_blob_service = BlockBlobService(account_name=args.get('account-name'),
                                          account_key=args.get('account-key'))

    # TODO: update this once enums are supported in commands first-class (task #115175885)
    public_access_types = {'none': None,
                           'blob': PublicAccess.Blob,
                           'container': PublicAccess.Container}
    try:
        public_access = public_access_types[args.get('container.public-access')] \
                        if args.get('container.public-access') \
                        else None
    except KeyError:
        raise IncorrectUsageError("container.public-access must be either none, blob or container")

    block_blob_service.create_container(args.get('container'), public_access=public_access)

    return block_blob_service.create_blob_from_path(
        args.get('container'),
        args.get('blob-name'),
        args.get('upload-from'),
        content_settings=ContentSettings(content_type=args.get('content-settings.type'), 
                                         content_disposition=args.get('content-settings.disposition'),
                                         content_encoding=args.get('content-settings.encoding'),
                                         content_language=args.get('content-settings.language'),
                                         content_md5=args.get('content-settings.md5'),
                                         cache_control=args.get('content-settings.cache-control')
                                         )
        )

@command('storage blob list')
@option('--account-name -an <name>', required=True)
@option('--account-key -ak <key>', required=True)
@option('--container -c <name>', required=True)
def list_blobs(args, unexpected): #pylint: disable=unused-argument
    from azure.storage.blob import BlockBlobService, PublicAccess, ContentSettings

    block_blob_service = BlockBlobService(account_name=args.get('account-name'),
                                          account_key=args.get('account-key'))

    blobs = block_blob_service.list_blobs(args.get('container'))
    return Serializer().serialize_data(blobs.items, "[Blob]")

@command('storage file create')
@option('--account-name -an <name>', required=True)
@option('--account-key -ak <key>', required=True)
@option('--share-name -sn <setting>', required=True)
@option('--file-name -fn <setting>', required=True)
@option('--local-file-name -lfn <setting>', required=True)
@option('--directory-name -dn <setting>')
def storage_file_create(args, unexpected): #pylint: disable=unused-argument
    from azure.storage.file import FileService

    file_service = FileService(account_name=args.get('account-name'),
                               account_key=args.get('account-key'))

    file_service.create_file_from_path(args.get('share-name'), 
                                       args.get('directory-name'), 
                                       args.get('file-name'),
                                       args.get('local-file-name'))
