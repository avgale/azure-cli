# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class IdentityProperties(Model):
    """IdentityProperties.

    :param type: Managed identity.
    :type type: str
    :param principal_id: The principal id of resource identity.
    :type principal_id: str
    :param tenant_id: The tenant identifier of resource.
    :type tenant_id: str
    :param client_secret_url: The client secret URL of the identity.
    :type client_secret_url: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'client_secret_url': {'key': 'clientSecretUrl', 'type': 'str'},
    }

    def __init__(self, type=None, principal_id=None, tenant_id=None, client_secret_url=None):
        self.type = type
        self.principal_id = principal_id
        self.tenant_id = tenant_id
        self.client_secret_url = client_secret_url
