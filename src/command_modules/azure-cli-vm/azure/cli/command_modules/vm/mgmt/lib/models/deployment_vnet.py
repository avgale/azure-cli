#pylint: skip-file
#pylint: skip-file
#pylint: skip-file
#pylint: skip-file
#pylint: skip-file
#pylint: skip-file
#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.15.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeploymentVNet(Model):
    """
    Deployment operation parameters.

    :param str uri: URI referencing the template. Default value:
     "https://azuretemplatedeploy.blob.core.windows.net/templatehost/CreateVNet/azuredeploy.json"
     .
    :param str content_version: If included it must match the ContentVersion
     in the template.
    :param str deployment_parameter_virtual_network_prefix_value: IP address
     prefix for the virtual network.
    :param str deployment_parameter_subnet_prefix_value: IP address prefix
     for the subnet.
    :param str deployment_parameter_virtual_network_name_value: Name of the
     virtual network.
    :param str deployment_parameter_subnet_name_value: Name of the subnet.
    :param str deployment_parameter_location_value: Location of the virtual
     network.
    :param str mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    """ 

    _validation = {
        'uri': {'required': True},
        'deployment_parameter_virtual_network_prefix_value': {'pattern': '^[\d\./]+$'},
        'deployment_parameter_subnet_prefix_value': {'pattern': '^[\d\./]+$'},
        'deployment_parameter_virtual_network_name_value': {'required': True, 'max_length': 80, 'min_length': 2, 'pattern': '^[-\w\._]+$'},
        'deployment_parameter_subnet_name_value': {'max_length': 80, 'min_length': 2, 'pattern': '^[-\w\._]+$'},
        'mode': {'required': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        'deployment_parameter_virtual_network_prefix_value': {'key': 'properties.parameters.virtualNetworkPrefix.value', 'type': 'str'},
        'deployment_parameter_subnet_prefix_value': {'key': 'properties.parameters.subnetPrefix.value', 'type': 'str'},
        'deployment_parameter_virtual_network_name_value': {'key': 'properties.parameters.virtualNetworkName.value', 'type': 'str'},
        'deployment_parameter_subnet_name_value': {'key': 'properties.parameters.subnetName.value', 'type': 'str'},
        'deployment_parameter_location_value': {'key': 'properties.parameters.location.value', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    def __init__(self, deployment_parameter_virtual_network_name_value, content_version=None, deployment_parameter_virtual_network_prefix_value=None, deployment_parameter_subnet_prefix_value=None, deployment_parameter_subnet_name_value=None, deployment_parameter_location_value=None, **kwargs):
        self.uri = "https://azuretemplatedeploy.blob.core.windows.net/templatehost/CreateVNet/azuredeploy.json"
        self.content_version = content_version
        self.deployment_parameter_virtual_network_prefix_value = deployment_parameter_virtual_network_prefix_value
        self.deployment_parameter_subnet_prefix_value = deployment_parameter_subnet_prefix_value
        self.deployment_parameter_virtual_network_name_value = deployment_parameter_virtual_network_name_value
        self.deployment_parameter_subnet_name_value = deployment_parameter_subnet_name_value
        self.deployment_parameter_location_value = deployment_parameter_location_value
        self.mode = "Incremental"
