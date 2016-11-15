# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
#pylint: skip-file

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeploymentRouteTable(Model):
    """
    Deployment operation parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar uri: URI referencing the template. Default value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreateRouteTable_2016-08-08/azuredeploy.json"
     .
    :vartype uri: str
    :param content_version: If included it must match the ContentVersion in
     the template.
    :type content_version: str
    :param location: Location for resource.
    :type location: str
    :param route_table_name: Name for route table.
    :type route_table_name: str
    :param tags: Tags object.
    :type tags: object
    :ivar mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    :vartype mode: str
    """ 

    _validation = {
        'uri': {'required': True, 'constant': True},
        'route_table_name': {'required': True},
        'mode': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        'location': {'key': 'properties.parameters.location.value', 'type': 'str'},
        'route_table_name': {'key': 'properties.parameters.routeTableName.value', 'type': 'str'},
        'tags': {'key': 'properties.parameters.tags.value', 'type': 'object'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    uri = "https://azuresdkci.blob.core.windows.net/templatehost/CreateRouteTable_2016-08-08/azuredeploy.json"

    mode = "Incremental"

    def __init__(self, route_table_name, content_version=None, location=None, tags=None):
        self.content_version = content_version
        self.location = location
        self.route_table_name = route_table_name
        self.tags = tags
