#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
#pylint: skip-file

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeploymentExpressRouteCircuit(Model):
    """
    Deployment operation parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar uri: URI referencing the template. Default value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreateExpressRouteCircuit_2016-08-08/azuredeploy.json"
     .
    :vartype uri: str
    :param content_version: If included it must match the ContentVersion in
     the template.
    :type content_version: str
    :param bandwidth_in_mbps: Bandwidth in Mbps of the circuit being created.
     It must exactly match one of the available bandwidth offers List
     ExpressRoute Service Providers API call.
    :type bandwidth_in_mbps: int
    :param circuit_name: Name of the ExpressRoute circuit
    :type circuit_name: str
    :param location: Location for resources.
    :type location: str
    :param peering_location: Name of the peering location. It must exactly
     match one of the available peering locations from List ExpressRoute
     Service Providers API call.
    :type peering_location: str
    :param service_provider_name: Name of the ExpressRoute Service Provider.
     It must exactly match one of the Service Providers from List
     ExpressRoute Service Providers API call.
    :type service_provider_name: str
    :param sku_family: Chosen SKU family of ExpressRoute circuit. Default
     value: "MeteredData" .
    :type sku_family: str
    :param sku_tier: SKU Tier of ExpressRoute circuit. Default value:
     "Standard" .
    :type sku_tier: str
    :param tags: Tags object.
    :type tags: object
    :ivar mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    :vartype mode: str
    """ 

    _validation = {
        'uri': {'required': True, 'constant': True},
        'bandwidth_in_mbps': {'required': True},
        'circuit_name': {'required': True},
        'peering_location': {'required': True},
        'service_provider_name': {'required': True},
        'mode': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        'bandwidth_in_mbps': {'key': 'properties.parameters.bandwidthInMbps.value', 'type': 'int'},
        'circuit_name': {'key': 'properties.parameters.circuitName.value', 'type': 'str'},
        'location': {'key': 'properties.parameters.location.value', 'type': 'str'},
        'peering_location': {'key': 'properties.parameters.peeringLocation.value', 'type': 'str'},
        'service_provider_name': {'key': 'properties.parameters.serviceProviderName.value', 'type': 'str'},
        'sku_family': {'key': 'properties.parameters.sku_family.value', 'type': 'str'},
        'sku_tier': {'key': 'properties.parameters.sku_tier.value', 'type': 'str'},
        'tags': {'key': 'properties.parameters.tags.value', 'type': 'object'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    uri = "https://azuresdkci.blob.core.windows.net/templatehost/CreateExpressRouteCircuit_2016-08-08/azuredeploy.json"

    mode = "Incremental"

    def __init__(self, bandwidth_in_mbps, circuit_name, peering_location, service_provider_name, content_version=None, location=None, sku_family="MeteredData", sku_tier="Standard", tags=None):
        self.content_version = content_version
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.circuit_name = circuit_name
        self.location = location
        self.peering_location = peering_location
        self.service_provider_name = service_provider_name
        self.sku_family = sku_family
        self.sku_tier = sku_tier
        self.tags = tags
