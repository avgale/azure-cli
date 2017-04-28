# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from .resource import Resource


class Lab(Resource):
    """A lab.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    :ivar default_storage_account: The lab's default storage account.
    :vartype default_storage_account: str
    :ivar default_premium_storage_account: The lab's default premium storage
     account.
    :vartype default_premium_storage_account: str
    :ivar artifacts_storage_account: The lab's artifact storage account.
    :vartype artifacts_storage_account: str
    :ivar premium_data_disk_storage_account: The lab's premium data disk
     storage account.
    :vartype premium_data_disk_storage_account: str
    :ivar vault_name: The lab's Key vault.
    :vartype vault_name: str
    :param lab_storage_type: Type of storage used by the lab. It can be either
     Premium or Standard. Default is Premium. Possible values include:
     'Standard', 'Premium'
    :type lab_storage_type: str or :class:`StorageType
     <devtestlabs.models.StorageType>`
    :ivar created_date: The creation date of the lab.
    :vartype created_date: datetime
    :param premium_data_disks: The setting to enable usage of premium data
     disks.
     When its value is 'Enabled', creation of standard or premium data disks is
     allowed.
     When its value is 'Disabled', only creation of standard data disks is
     allowed. Possible values include: 'Disabled', 'Enabled'
    :type premium_data_disks: str or :class:`PremiumDataDisk
     <devtestlabs.models.PremiumDataDisk>`
    :param provisioning_state: The provisioning status of the resource.
    :type provisioning_state: str
    :param unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :type unique_identifier: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'default_storage_account': {'readonly': True},
        'default_premium_storage_account': {'readonly': True},
        'artifacts_storage_account': {'readonly': True},
        'premium_data_disk_storage_account': {'readonly': True},
        'vault_name': {'readonly': True},
        'created_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'default_storage_account': {'key': 'properties.defaultStorageAccount', 'type': 'str'},
        'default_premium_storage_account': {'key': 'properties.defaultPremiumStorageAccount', 'type': 'str'},
        'artifacts_storage_account': {'key': 'properties.artifactsStorageAccount', 'type': 'str'},
        'premium_data_disk_storage_account': {'key': 'properties.premiumDataDiskStorageAccount', 'type': 'str'},
        'vault_name': {'key': 'properties.vaultName', 'type': 'str'},
        'lab_storage_type': {'key': 'properties.labStorageType', 'type': 'str'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'premium_data_disks': {'key': 'properties.premiumDataDisks', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
    }

    def __init__(self, location=None, tags=None, lab_storage_type=None, premium_data_disks=None, provisioning_state=None, unique_identifier=None):
        super(Lab, self).__init__(location=location, tags=tags)
        self.default_storage_account = None
        self.default_premium_storage_account = None
        self.artifacts_storage_account = None
        self.premium_data_disk_storage_account = None
        self.vault_name = None
        self.lab_storage_type = lab_storage_type
        self.created_date = None
        self.premium_data_disks = premium_data_disks
        self.provisioning_state = provisioning_state
        self.unique_identifier = unique_identifier
