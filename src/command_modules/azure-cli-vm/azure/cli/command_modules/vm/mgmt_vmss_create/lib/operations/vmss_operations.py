#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_operation import AzureOperationPoller
import uuid

from .. import models


class VMSSOperations(object):
    """VMSSOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def create_or_update(
            self, resource_group_name, deployment_name, admin_username, name, content_version=None, admin_password=None, authentication_type="password", custom_os_disk_type="windows", custom_os_disk_uri=None, dns_name_for_public_ip=None, dns_name_type="none", instance_count="2", load_balancer_backend_pool_name=None, load_balancer_name=None, load_balancer_nat_pool_name=None, load_balancer_type="new", location=None, nat_backend_port="22", nat_end_port="50099", nat_start_port="50000", os_disk_name="osdiskimage", os_disk_type="provided", os_offer="WindowsServer", os_publisher="MicrosoftWindowsServer", os_sku="2012-R2-Datacenter", os_type="Win2012R2Datacenter", os_version="latest", overprovision="true", private_ip_address=None, private_ip_address_allocation="dynamic", public_ip_address_allocation="dynamic", public_ip_address_name=None, public_ip_address_type="new", ssh_dest_key_path=None, ssh_key_value=None, storage_caching="ReadOnly", storage_container_name="vhds", storage_redundancy_type="Standard_LRS", subnet_ip_address_prefix="10.0.0.0/24", subnet_name=None, upgrade_policy_mode="manual", virtual_network_ip_address_prefix="10.0.0.0/16", virtual_network_name=None, virtual_network_type="new", vm_sku="Standard_D1_v2", custom_headers=None, raw=False, **operation_config):
        """
        Create or update a virtual machine.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param admin_username: Username for the Virtual Machine.
        :type admin_username: str
        :param name: The VM name.
        :type name: str
        :param content_version: If included it must match the ContentVersion
         in the template.
        :type content_version: str
        :param admin_password: Password for the Virtual Machine.  Required if
         SSH (Linux only) is not specified.
        :type admin_password: str
        :param authentication_type: Password or SSH Public Key
         authentication. Possible values include: 'password', 'ssh'
        :type authentication_type: str
        :param custom_os_disk_type: Custom image OS type. Possible values
         include: 'windows', 'linux'
        :type custom_os_disk_type: str
        :param custom_os_disk_uri: URI to a custom disk image.
        :type custom_os_disk_uri: str
        :param dns_name_for_public_ip: Globally unique DNS Name for the
         Public IP used to access the Virtual Machine.  Requires a new public
         IP to be created by setting Public IP Address Type to New.
        :type dns_name_for_public_ip: str
        :param dns_name_type: Associate VMs with a public IP address to a DNS
         name. Possible values include: 'none', 'new'
        :type dns_name_type: str
        :param instance_count: Number of VMs in scale set.
        :type instance_count: str
        :param load_balancer_backend_pool_name: Name of load balancer backend
         pool.
        :type load_balancer_backend_pool_name: str
        :param load_balancer_name: Name for load balancer.
        :type load_balancer_name: str
        :param load_balancer_nat_pool_name: Name of load balancer NAT
         (network address translation) pool.
        :type load_balancer_nat_pool_name: str
        :param load_balancer_type: Whether to use an existing load balancer,
         create a new one, or use no load balancer. Possible values include:
         'new', 'existing', 'none'
        :type load_balancer_type: str
        :param location: Location for VM resources.
        :type location: str
        :param nat_backend_port: End of NAT port range.
        :type nat_backend_port: str
        :param nat_end_port: End of NAT port range.
        :type nat_end_port: str
        :param nat_start_port: Begining of NAT port range.
        :type nat_start_port: str
        :param os_disk_name: Name of new VM OS disk.
        :type os_disk_name: str
        :param os_disk_type: Use a custom image URI from the OS Disk URI
         parameter or use a provider's image. Possible values include:
         'provided', 'custom'
        :type os_disk_type: str
        :param os_offer: The OS Offer to install.
        :type os_offer: str
        :param os_publisher: The OS publisher of the OS image.
        :type os_publisher: str
        :param os_sku: The OS SKU to install.
        :type os_sku: str
        :param os_type: Common OS choices.  Choose 'Custom' to specify an
         image with the osPublisher, osOffer, osSKU, and osVersion
         parameters. Possible values include: 'Win2012R2Datacenter',
         'Win2012Datacenter', 'Win2008R2SP1', 'Custom'
        :type os_type: str
        :param os_version: The OS version to install.
        :type os_version: str
        :param overprovision: Overprovision option (see
         https://azure.microsoft.com/en-us/documentation/articles/virtual-machine-scale-sets-overview/
         for details). Possible values include: 'true', 'false', 'True',
         'False'
        :type overprovision: str
        :param private_ip_address: The private IP address to use with Private
         IP Address Allocation type Static.
        :type private_ip_address: str
        :param private_ip_address_allocation: Private IP address allocation
         method. Possible values include: 'dynamic', 'static'
        :type private_ip_address_allocation: str
        :param public_ip_address_allocation: Public IP address allocation
         method. Possible values include: 'dynamic', 'static'
        :type public_ip_address_allocation: str
        :param public_ip_address_name: Name of public IP address to use.
        :type public_ip_address_name: str
        :param public_ip_address_type: Use a public IP Address for the VM
         Nic. Possible values include: 'none', 'new', 'existing'
        :type public_ip_address_type: str
        :param ssh_dest_key_path: Destination file path on VM for SSH key.
        :type ssh_dest_key_path: str
        :param ssh_key_value: SSH key file data.
        :type ssh_key_value: str
        :param storage_caching: Storage caching type. Possible values
         include: 'ReadOnly', 'ReadWrite'
        :type storage_caching: str
        :param storage_container_name: Name of storage container for the VM
         OS disk.
        :type storage_container_name: str
        :param storage_redundancy_type: The VM storage type (Standard_LRS,
         Standard_GRS, Standard_RAGRS).
        :type storage_redundancy_type: str
        :param subnet_ip_address_prefix: The subnet address prefix in CIDR
         format.
        :type subnet_ip_address_prefix: str
        :param subnet_name: The subnet name.
        :type subnet_name: str
        :param upgrade_policy_mode: Manual or Automatic upgrade mode.
         Possible values include: 'manual', 'automatic'
        :type upgrade_policy_mode: str
        :param virtual_network_ip_address_prefix: The virtual network IP
         address prefix in CIDR format.
        :type virtual_network_ip_address_prefix: str
        :param virtual_network_name: Name of virtual network to add VM to.
        :type virtual_network_name: str
        :param virtual_network_type: Whether to use an existing VNet or
         create a new one. Possible values include: 'new', 'existing'
        :type virtual_network_type: str
        :param vm_sku: Size of VMs in the VM Scale Set.  See
         https://azure.microsoft.com/en-us/pricing/details/virtual-machines/
         for size info.
        :type vm_sku: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`DeploymentExtended
         <mynamespace.models.DeploymentExtended>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        parameters = models.DeploymentVMSS(content_version=content_version, admin_password=admin_password, admin_username=admin_username, authentication_type=authentication_type, custom_os_disk_type=custom_os_disk_type, custom_os_disk_uri=custom_os_disk_uri, dns_name_for_public_ip=dns_name_for_public_ip, dns_name_type=dns_name_type, instance_count=instance_count, load_balancer_backend_pool_name=load_balancer_backend_pool_name, load_balancer_name=load_balancer_name, load_balancer_nat_pool_name=load_balancer_nat_pool_name, load_balancer_type=load_balancer_type, location=location, name=name, nat_backend_port=nat_backend_port, nat_end_port=nat_end_port, nat_start_port=nat_start_port, os_disk_name=os_disk_name, os_disk_type=os_disk_type, os_offer=os_offer, os_publisher=os_publisher, os_sku=os_sku, os_type=os_type, os_version=os_version, overprovision=overprovision, private_ip_address=private_ip_address, private_ip_address_allocation=private_ip_address_allocation, public_ip_address_allocation=public_ip_address_allocation, public_ip_address_name=public_ip_address_name, public_ip_address_type=public_ip_address_type, ssh_dest_key_path=ssh_dest_key_path, ssh_key_value=ssh_key_value, storage_caching=storage_caching, storage_container_name=storage_container_name, storage_redundancy_type=storage_redundancy_type, subnet_ip_address_prefix=subnet_ip_address_prefix, subnet_name=subnet_name, upgrade_policy_mode=upgrade_policy_mode, virtual_network_ip_address_prefix=virtual_network_ip_address_prefix, virtual_network_name=virtual_network_name, virtual_network_type=virtual_network_type, vm_sku=vm_sku)

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deployments/{deploymentName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=64, min_length=1, pattern='^[-\w\._]+$'),
            'deploymentName': self._serialize.url("deployment_name", deployment_name, 'str', max_length=64, min_length=1, pattern='^[-\w\._]+$'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'DeploymentVMSS')

        # Construct and send request
        def long_running_send():

            request = self._client.put(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 201]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            deserialized = None

            if response.status_code == 200:
                deserialized = self._deserialize('DeploymentExtended', response)
            if response.status_code == 201:
                deserialized = self._deserialize('DeploymentExtended', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)
