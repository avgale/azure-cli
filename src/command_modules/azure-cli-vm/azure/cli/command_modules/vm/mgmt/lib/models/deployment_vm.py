#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .deployment_parameter_artifacts_location import DeploymentParameterArtifactsLocation
from msrest.serialization import Model


class DeploymentVM(Model):
    """
    Deployment operation parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar uri: URI referencing the template. Default value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreateVM/azuredeploy.json"
     .
    :vartype uri: str
    :param content_version: If included it must match the ContentVersion in
     the template.
    :type content_version: str
    :param storage_container_name: Name of storage container for the VM OS
     disk.
    :type storage_container_name: str
    :param virtual_network_name: Name of virtual network to add VM to.
    :type virtual_network_name: str
    :param subnet_ip_address_prefix: The subnet address type.
    :type subnet_ip_address_prefix: str
    :param private_ip_address_allocation: Dynamic of Static private IP
     address allocation.
    :type private_ip_address_allocation: str
    :param dns_name_for_public_ip: Globally unique DNS Name for the Public IP
     used to access the Virtual Machine.
    :type dns_name_for_public_ip: str
    :param storage_account_type: Whether to use an existing storage account
     or create a new one.
    :type storage_account_type: str
    :param os_disk_uri: URI for a custom VHD image.
    :type os_disk_uri: str
    :ivar _artifacts_location:
    :vartype _artifacts_location:
     :class:`DeploymentParameterArtifactsLocation <mynamespace.models.DeploymentParameterArtifactsLocation>`
    :param name: The VM resource name.
    :type name: str
    :param virtual_network_type: Whether to use an existing VNet or create a
     new one.
    :type virtual_network_type: str
    :param admin_password: Password for the Virtual Machine.
    :type admin_password: str
    :param os_sku: The OS SKU to install.
    :type os_sku: str
    :param subnet_name: The subnet name.
    :type subnet_name: str
    :param os_type: Common OS choices.  Choose 'Custom' to specify an image
     with the osPublisher, osOffer, osSKU, and osVersion parameters.
    :type os_type: str
    :param admin_username: Username for the Virtual Machine.
    :type admin_username: str
    :param os_version: The OS version to install.
    :type os_version: str
    :param os_disk_name: Name of new VM OS disk.
    :type os_disk_name: str
    :param ssh_key_path: VM file path for SSH key.
    :type ssh_key_path: str
    :param os_offer: The OS Offer to install.
    :type os_offer: str
    :param public_ip_address_allocation: Dynamic or Static public IP address
     allocation.
    :type public_ip_address_allocation: str
    :param authentication_type: Authentication method: password-only or add
     ssh-keys (Linux-only).
    :type authentication_type: str
    :param storage_account_name: Name of storage account for the VM OS disk.
    :type storage_account_name: str
    :param storage_redundancy_type: The VM storage type.
    :type storage_redundancy_type: str
    :param size: The VM Size that should be created  (e.g. Standard_A2)
    :type size: str
    :param public_ip_address_type: Use a public IP Address for the VM Nic.
     (new, existing or none).
    :type public_ip_address_type: str
    :param virtual_network_ip_address_prefix: The IP address prefix.
    :type virtual_network_ip_address_prefix: str
    :param availability_set_id: Existing availability set for the VM.
    :type availability_set_id: str
    :param ssh_key_value: SSH key file data.
    :type ssh_key_value: str
    :param location: Location for VM resources.
    :type location: str
    :param os_publisher: The OS publisher of the OS image.
    :type os_publisher: str
    :param availability_set_type: Flag to add the VM to an existing
     availability set.
    :type availability_set_type: str
    :param public_ip_address_name: Name of public IP address to use.
    :type public_ip_address_name: str
    :param dns_name_type: Associate VMs with a public IP address to a DNS
     name (new or none).
    :type dns_name_type: str
    :ivar mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    :vartype mode: str
    """ 

    _validation = {
        'uri': {'required': True, 'constant': True},
        '_artifacts_location': {'constant': True},
        'name': {'required': True},
        'admin_password': {'required': True},
        'admin_username': {'required': True},
        'mode': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        'storage_container_name': {'key': 'properties.parameters.storageContainerName.value', 'type': 'str'},
        'virtual_network_name': {'key': 'properties.parameters.virtualNetworkName.value', 'type': 'str'},
        'subnet_ip_address_prefix': {'key': 'properties.parameters.subnetIpAddressPrefix.value', 'type': 'str'},
        'private_ip_address_allocation': {'key': 'properties.parameters.privateIpAddressAllocation.value', 'type': 'str'},
        'dns_name_for_public_ip': {'key': 'properties.parameters.dnsNameForPublicIP.value', 'type': 'str'},
        'storage_account_type': {'key': 'properties.parameters.storageAccountType.value', 'type': 'str'},
        'os_disk_uri': {'key': 'properties.parameters.osDiskUri.value', 'type': 'str'},
        '_artifacts_location': {'key': 'properties.parameters._artifactsLocation', 'type': 'DeploymentParameterArtifactsLocation'},
        'name': {'key': 'properties.parameters.name.value', 'type': 'str'},
        'virtual_network_type': {'key': 'properties.parameters.virtualNetworkType.value', 'type': 'str'},
        'admin_password': {'key': 'properties.parameters.adminPassword.value', 'type': 'str'},
        'os_sku': {'key': 'properties.parameters.osSKU.value', 'type': 'str'},
        'subnet_name': {'key': 'properties.parameters.subnetName.value', 'type': 'str'},
        'os_type': {'key': 'properties.parameters.osType.value', 'type': 'str'},
        'admin_username': {'key': 'properties.parameters.adminUsername.value', 'type': 'str'},
        'os_version': {'key': 'properties.parameters.osVersion.value', 'type': 'str'},
        'os_disk_name': {'key': 'properties.parameters.osDiskName.value', 'type': 'str'},
        'ssh_key_path': {'key': 'properties.parameters.sshKeyPath.value', 'type': 'str'},
        'os_offer': {'key': 'properties.parameters.osOffer.value', 'type': 'str'},
        'public_ip_address_allocation': {'key': 'properties.parameters.publicIpAddressAllocation.value', 'type': 'str'},
        'authentication_type': {'key': 'properties.parameters.authenticationType.value', 'type': 'str'},
        'storage_account_name': {'key': 'properties.parameters.storageAccountName.value', 'type': 'str'},
        'storage_redundancy_type': {'key': 'properties.parameters.storageRedundancyType.value', 'type': 'str'},
        'size': {'key': 'properties.parameters.size.value', 'type': 'str'},
        'public_ip_address_type': {'key': 'properties.parameters.publicIpAddressType.value', 'type': 'str'},
        'virtual_network_ip_address_prefix': {'key': 'properties.parameters.virtualNetworkIpAddressPrefix.value', 'type': 'str'},
        'availability_set_id': {'key': 'properties.parameters.availabilitySetId.value', 'type': 'str'},
        'ssh_key_value': {'key': 'properties.parameters.sshKeyValue.value', 'type': 'str'},
        'location': {'key': 'properties.parameters.location.value', 'type': 'str'},
        'os_publisher': {'key': 'properties.parameters.osPublisher.value', 'type': 'str'},
        'availability_set_type': {'key': 'properties.parameters.availabilitySetType.value', 'type': 'str'},
        'public_ip_address_name': {'key': 'properties.parameters.publicIpAddressName.value', 'type': 'str'},
        'dns_name_type': {'key': 'properties.parameters.dnsNameType.value', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    uri = "https://azuresdkci.blob.core.windows.net/templatehost/CreateVM/azuredeploy.json"

    _artifacts_location = DeploymentParameterArtifactsLocation()

    mode = "Incremental"

    def __init__(self, name, admin_password, admin_username, content_version=None, storage_container_name=None, virtual_network_name=None, subnet_ip_address_prefix=None, private_ip_address_allocation=None, dns_name_for_public_ip=None, storage_account_type=None, os_disk_uri=None, virtual_network_type=None, os_sku=None, subnet_name=None, os_type=None, os_version=None, os_disk_name=None, ssh_key_path=None, os_offer=None, public_ip_address_allocation=None, authentication_type=None, storage_account_name=None, storage_redundancy_type=None, size=None, public_ip_address_type=None, virtual_network_ip_address_prefix=None, availability_set_id=None, ssh_key_value=None, location=None, os_publisher=None, availability_set_type=None, public_ip_address_name=None, dns_name_type=None):
        self.content_version = content_version
        self.storage_container_name = storage_container_name
        self.virtual_network_name = virtual_network_name
        self.subnet_ip_address_prefix = subnet_ip_address_prefix
        self.private_ip_address_allocation = private_ip_address_allocation
        self.dns_name_for_public_ip = dns_name_for_public_ip
        self.storage_account_type = storage_account_type
        self.os_disk_uri = os_disk_uri
        self.name = name
        self.virtual_network_type = virtual_network_type
        self.admin_password = admin_password
        self.os_sku = os_sku
        self.subnet_name = subnet_name
        self.os_type = os_type
        self.admin_username = admin_username
        self.os_version = os_version
        self.os_disk_name = os_disk_name
        self.ssh_key_path = ssh_key_path
        self.os_offer = os_offer
        self.public_ip_address_allocation = public_ip_address_allocation
        self.authentication_type = authentication_type
        self.storage_account_name = storage_account_name
        self.storage_redundancy_type = storage_redundancy_type
        self.size = size
        self.public_ip_address_type = public_ip_address_type
        self.virtual_network_ip_address_prefix = virtual_network_ip_address_prefix
        self.availability_set_id = availability_set_id
        self.ssh_key_value = ssh_key_value
        self.location = location
        self.os_publisher = os_publisher
        self.availability_set_type = availability_set_type
        self.public_ip_address_name = public_ip_address_name
        self.dns_name_type = dns_name_type
