#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

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
    :ivar _artifacts_location: Container URI of of the template. Default
     value: "https://azuresdkci.blob.core.windows.net/templatehost/CreateVM" .
    :vartype _artifacts_location: str
    :param admin_password: Password for the Virtual Machine.  Required if SSH
     (Linux only) is not specified.
    :type admin_password: str
    :param admin_username: Username for the Virtual Machine.
    :type admin_username: str
    :param authentication_type: Password or SSH Public Key authentication.
     Possible values include: 'password', 'sshkey'. Default value: "password"
     .
    :type authentication_type: str
    :param availability_set_id: Existing availability set for the VM.
    :type availability_set_id: str
    :param availability_set_type: Flag to add the VM to an existing
     availability set. Possible values include: 'none', 'existing'. Default
     value: "none" .
    :type availability_set_type: str
    :param dns_name_for_public_ip: Globally unique DNS Name for the Public IP
     used to access the Virtual Machine.  Requires a new public IP to be
     created by setting Public IP Address Type to New.
    :type dns_name_for_public_ip: str
    :param dns_name_type: Associate VMs with a public IP address to a DNS
     name. Possible values include: 'none', 'new'. Default value: "none" .
    :type dns_name_type: str
    :param location: Location for VM resources.
    :type location: str
    :param name: The VM name.
    :type name: str
    :param os_disk_name: Name of new VM OS disk. Default value: "osdiskimage"
     .
    :type os_disk_name: str
    :param os_disk_uri: URI for a custom VHD image.
    :type os_disk_uri: str
    :param os_offer: The OS Offer to install. Default value: "WindowsServer" .
    :type os_offer: str
    :param os_publisher: The OS publisher of the OS image. Default value:
     "MicrosoftWindowsServer" .
    :type os_publisher: str
    :param os_sku: The OS SKU to install. Default value: "2012-R2-Datacenter"
     .
    :type os_sku: str
    :param os_type: Common OS choices.  Choose 'Custom' to specify an image
     with the osPublisher, osOffer, osSKU, and osVersion parameters. Possible
     values include: 'Win2012R2Datacenter', 'Win2012Datacenter',
     'Win2008R2SP1', 'Custom'. Default value: "Win2012R2Datacenter" .
    :type os_type: str
    :param os_version: The OS version to install. Default value: "latest" .
    :type os_version: str
    :param private_ip_address_allocation: Private IP address allocation
     method. Possible values include: 'Dynamic', 'Static'. Default value:
     "Dynamic" .
    :type private_ip_address_allocation: str
    :param public_ip_address_allocation: Public IP address allocation method.
     Possible values include: 'Dynamic', 'Static'. Default value: "Dynamic" .
    :type public_ip_address_allocation: str
    :param public_ip_address_name: Name of public IP address to use.
    :type public_ip_address_name: str
    :param public_ip_address_type: Use a public IP Address for the VM Nic.
     Possible values include: 'none', 'new', 'existing'. Default value:
     "none" .
    :type public_ip_address_type: str
    :param size: The VM Size that should be created.  See
     https://azure.microsoft.com/en-us/pricing/details/virtual-machines/ for
     size info. Default value: "Standard_A2" .
    :type size: str
    :param ssh_dest_key_path: Destination file path on VM for SSH key.
    :type ssh_dest_key_path: str
    :param ssh_key_value: SSH key file data.
    :type ssh_key_value: str
    :param storage_account_name: Name of storage account for the VM OS disk.
    :type storage_account_name: str
    :param storage_account_type: Whether to use an existing storage account
     or create a new one. Possible values include: 'new', 'existing'. Default
     value: "new" .
    :type storage_account_type: str
    :param storage_container_name: Name of storage container for the VM OS
     disk. Default value: "vhds" .
    :type storage_container_name: str
    :param storage_redundancy_type: The VM storage type (Standard_LRS,
     Standard_GRS, Standard_RAGRS). Default value: "Standard_LRS" .
    :type storage_redundancy_type: str
    :param subnet_ip_address_prefix: The subnet address prefix in CIDR
     format. Default value: "10.0.0.0/24" .
    :type subnet_ip_address_prefix: str
    :param subnet_name: The subnet name.
    :type subnet_name: str
    :param virtual_network_ip_address_prefix: The virtual network IP address
     prefix in CIDR format. Default value: "10.0.0.0/16" .
    :type virtual_network_ip_address_prefix: str
    :param virtual_network_name: Name of virtual network to add VM to.
    :type virtual_network_name: str
    :param virtual_network_type: Whether to use an existing VNet or create a
     new one. Possible values include: 'new', 'existing'. Default value:
     "new" .
    :type virtual_network_type: str
    :ivar mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    :vartype mode: str
    """ 

    _validation = {
        'uri': {'required': True, 'constant': True},
        '_artifacts_location': {'required': True, 'constant': True},
        'admin_username': {'required': True},
        'name': {'required': True},
        'mode': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        '_artifacts_location': {'key': 'properties.parameters._artifactsLocation.value', 'type': 'str'},
        'admin_password': {'key': 'properties.parameters.adminPassword.value', 'type': 'str'},
        'admin_username': {'key': 'properties.parameters.adminUsername.value', 'type': 'str'},
        'authentication_type': {'key': 'properties.parameters.authenticationType.value', 'type': 'str'},
        'availability_set_id': {'key': 'properties.parameters.availabilitySetId.value', 'type': 'str'},
        'availability_set_type': {'key': 'properties.parameters.availabilitySetType.value', 'type': 'str'},
        'dns_name_for_public_ip': {'key': 'properties.parameters.dnsNameForPublicIP.value', 'type': 'str'},
        'dns_name_type': {'key': 'properties.parameters.dnsNameType.value', 'type': 'str'},
        'location': {'key': 'properties.parameters.location.value', 'type': 'str'},
        'name': {'key': 'properties.parameters.name.value', 'type': 'str'},
        'os_disk_name': {'key': 'properties.parameters.osDiskName.value', 'type': 'str'},
        'os_disk_uri': {'key': 'properties.parameters.osDiskUri.value', 'type': 'str'},
        'os_offer': {'key': 'properties.parameters.osOffer.value', 'type': 'str'},
        'os_publisher': {'key': 'properties.parameters.osPublisher.value', 'type': 'str'},
        'os_sku': {'key': 'properties.parameters.osSKU.value', 'type': 'str'},
        'os_type': {'key': 'properties.parameters.osType.value', 'type': 'str'},
        'os_version': {'key': 'properties.parameters.osVersion.value', 'type': 'str'},
        'private_ip_address_allocation': {'key': 'properties.parameters.privateIpAddressAllocation.value', 'type': 'str'},
        'public_ip_address_allocation': {'key': 'properties.parameters.publicIpAddressAllocation.value', 'type': 'str'},
        'public_ip_address_name': {'key': 'properties.parameters.publicIpAddressName.value', 'type': 'str'},
        'public_ip_address_type': {'key': 'properties.parameters.publicIpAddressType.value', 'type': 'str'},
        'size': {'key': 'properties.parameters.size.value', 'type': 'str'},
        'ssh_dest_key_path': {'key': 'properties.parameters.sshDestKeyPath.value', 'type': 'str'},
        'ssh_key_value': {'key': 'properties.parameters.sshKeyValue.value', 'type': 'str'},
        'storage_account_name': {'key': 'properties.parameters.storageAccountName.value', 'type': 'str'},
        'storage_account_type': {'key': 'properties.parameters.storageAccountType.value', 'type': 'str'},
        'storage_container_name': {'key': 'properties.parameters.storageContainerName.value', 'type': 'str'},
        'storage_redundancy_type': {'key': 'properties.parameters.storageRedundancyType.value', 'type': 'str'},
        'subnet_ip_address_prefix': {'key': 'properties.parameters.subnetIpAddressPrefix.value', 'type': 'str'},
        'subnet_name': {'key': 'properties.parameters.subnetName.value', 'type': 'str'},
        'virtual_network_ip_address_prefix': {'key': 'properties.parameters.virtualNetworkIpAddressPrefix.value', 'type': 'str'},
        'virtual_network_name': {'key': 'properties.parameters.virtualNetworkName.value', 'type': 'str'},
        'virtual_network_type': {'key': 'properties.parameters.virtualNetworkType.value', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    uri = "https://azuresdkci.blob.core.windows.net/templatehost/CreateVM/azuredeploy.json"

    _artifacts_location = "https://azuresdkci.blob.core.windows.net/templatehost/CreateVM"

    mode = "Incremental"

    def __init__(self, admin_username, name, content_version=None, admin_password=None, authentication_type="password", availability_set_id=None, availability_set_type="none", dns_name_for_public_ip=None, dns_name_type="none", location=None, os_disk_name="osdiskimage", os_disk_uri=None, os_offer="WindowsServer", os_publisher="MicrosoftWindowsServer", os_sku="2012-R2-Datacenter", os_type="Win2012R2Datacenter", os_version="latest", private_ip_address_allocation="Dynamic", public_ip_address_allocation="Dynamic", public_ip_address_name=None, public_ip_address_type="none", size="Standard_A2", ssh_dest_key_path=None, ssh_key_value=None, storage_account_name=None, storage_account_type="new", storage_container_name="vhds", storage_redundancy_type="Standard_LRS", subnet_ip_address_prefix="10.0.0.0/24", subnet_name=None, virtual_network_ip_address_prefix="10.0.0.0/16", virtual_network_name=None, virtual_network_type="new"):
        self.content_version = content_version
        self.admin_password = admin_password
        self.admin_username = admin_username
        self.authentication_type = authentication_type
        self.availability_set_id = availability_set_id
        self.availability_set_type = availability_set_type
        self.dns_name_for_public_ip = dns_name_for_public_ip
        self.dns_name_type = dns_name_type
        self.location = location
        self.name = name
        self.os_disk_name = os_disk_name
        self.os_disk_uri = os_disk_uri
        self.os_offer = os_offer
        self.os_publisher = os_publisher
        self.os_sku = os_sku
        self.os_type = os_type
        self.os_version = os_version
        self.private_ip_address_allocation = private_ip_address_allocation
        self.public_ip_address_allocation = public_ip_address_allocation
        self.public_ip_address_name = public_ip_address_name
        self.public_ip_address_type = public_ip_address_type
        self.size = size
        self.ssh_dest_key_path = ssh_dest_key_path
        self.ssh_key_value = ssh_key_value
        self.storage_account_name = storage_account_name
        self.storage_account_type = storage_account_type
        self.storage_container_name = storage_container_name
        self.storage_redundancy_type = storage_redundancy_type
        self.subnet_ip_address_prefix = subnet_ip_address_prefix
        self.subnet_name = subnet_name
        self.virtual_network_ip_address_prefix = virtual_network_ip_address_prefix
        self.virtual_network_name = virtual_network_name
        self.virtual_network_type = virtual_network_type
