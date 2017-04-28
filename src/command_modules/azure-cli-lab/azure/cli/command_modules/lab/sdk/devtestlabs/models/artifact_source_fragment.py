# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from .resource import Resource


class ArtifactSourceFragment(Resource):
    """Properties of an artifact source.

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
    :param display_name: The artifact source's display name.
    :type display_name: str
    :param uri: The artifact source's URI.
    :type uri: str
    :param source_type: The artifact source's type. Possible values include:
     'VsoGit', 'GitHub'
    :type source_type: str or :class:`SourceControlType
     <devtestlabs.models.SourceControlType>`
    :param folder_path: The folder containing artifacts.
    :type folder_path: str
    :param arm_template_folder_path: The folder containing Azure Resource
     Manager templates.
    :type arm_template_folder_path: str
    :param branch_ref: The artifact source's branch reference.
    :type branch_ref: str
    :param security_token: The security token to authenticate to the artifact
     source.
    :type security_token: str
    :param status: Indicates if the artifact source is enabled (values:
     Enabled, Disabled). Possible values include: 'Enabled', 'Disabled'
    :type status: str or :class:`EnableStatus
     <devtestlabs.models.EnableStatus>`
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
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'uri': {'key': 'properties.uri', 'type': 'str'},
        'source_type': {'key': 'properties.sourceType', 'type': 'str'},
        'folder_path': {'key': 'properties.folderPath', 'type': 'str'},
        'arm_template_folder_path': {'key': 'properties.armTemplateFolderPath', 'type': 'str'},
        'branch_ref': {'key': 'properties.branchRef', 'type': 'str'},
        'security_token': {'key': 'properties.securityToken', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
    }

    def __init__(self, location=None, tags=None, display_name=None, uri=None, source_type=None, folder_path=None, arm_template_folder_path=None, branch_ref=None, security_token=None, status=None, provisioning_state=None, unique_identifier=None):
        super(ArtifactSourceFragment, self).__init__(location=location, tags=tags)
        self.display_name = display_name
        self.uri = uri
        self.source_type = source_type
        self.folder_path = folder_path
        self.arm_template_folder_path = arm_template_folder_path
        self.branch_ref = branch_ref
        self.security_token = security_token
        self.status = status
        self.provisioning_state = provisioning_state
        self.unique_identifier = unique_identifier
