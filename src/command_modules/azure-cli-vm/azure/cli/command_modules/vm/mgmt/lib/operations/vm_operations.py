#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_operation import AzureOperationPoller
import uuid

from .. import models


class VMOperations(object):
    """VMOperations operations.

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
            self, resource_group_name, deployment_name, name, admin_password, admin_username, content_version=None, storage_container_name=None, virtual_network_name=None, subnet_ip_address_prefix=None, private_ip_address_allocation=None, dns_name_for_public_ip=None, storage_account_type=None, os_disk_uri=None, virtual_network_type=None, os_sku=None, subnet_name=None, os_type=None, os_version=None, os_disk_name=None, ssh_key_path=None, os_offer=None, public_ip_address_allocation=None, authentication_type=None, storage_account_name=None, storage_redundancy_type=None, size=None, public_ip_address_type=None, virtual_network_ip_address_prefix=None, availability_set_id=None, ssh_key_value=None, location=None, os_publisher=None, availability_set_type=None, public_ip_address_name=None, dns_name_type=None, custom_headers={}, raw=False, **operation_config):
        """
        Create or update a virtual machine.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param name: The VM resource name.
        :type name: str
        :param admin_password: Password for the Virtual Machine.
        :type admin_password: str
        :param admin_username: Username for the Virtual Machine.
        :type admin_username: str
        :param content_version: If included it must match the ContentVersion
         in the template.
        :type content_version: str
        :param storage_container_name: Name of storage container for the VM
         OS disk.
        :type storage_container_name: str
        :param virtual_network_name: Name of virtual network to add VM to.
        :type virtual_network_name: str
        :param subnet_ip_address_prefix: The subnet address type.
        :type subnet_ip_address_prefix: str
        :param private_ip_address_allocation: Dynamic of Static private IP
         address allocation.
        :type private_ip_address_allocation: str
        :param dns_name_for_public_ip: Globally unique DNS Name for the
         Public IP used to access the Virtual Machine.
        :type dns_name_for_public_ip: str
        :param storage_account_type: Whether to use an existing storage
         account or create a new one.
        :type storage_account_type: str
        :param os_disk_uri: URI for a custom VHD image.
        :type os_disk_uri: str
        :param virtual_network_type: Whether to use an existing VNet or
         create a new one.
        :type virtual_network_type: str
        :param os_sku: The OS SKU to install.
        :type os_sku: str
        :param subnet_name: The subnet name.
        :type subnet_name: str
        :param os_type: Common OS choices.  Choose 'Custom' to specify an
         image with the osPublisher, osOffer, osSKU, and osVersion parameters.
        :type os_type: str
        :param os_version: The OS version to install.
        :type os_version: str
        :param os_disk_name: Name of new VM OS disk.
        :type os_disk_name: str
        :param ssh_key_path: VM file path for SSH key.
        :type ssh_key_path: str
        :param os_offer: The OS Offer to install.
        :type os_offer: str
        :param public_ip_address_allocation: Dynamic or Static public IP
         address allocation.
        :type public_ip_address_allocation: str
        :param authentication_type: Authentication method: password-only or
         add ssh-keys (Linux-only).
        :type authentication_type: str
        :param storage_account_name: Name of storage account for the VM OS
         disk.
        :type storage_account_name: str
        :param storage_redundancy_type: The VM storage type.
        :type storage_redundancy_type: str
        :param size: The VM Size that should be created.
        :type size: str
        :param public_ip_address_type: Use a public IP Address for the VM
         Nic. (new, existing or none).
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
        parameters = models.DeploymentVM(content_version=content_version, storage_container_name=storage_container_name, virtual_network_name=virtual_network_name, subnet_ip_address_prefix=subnet_ip_address_prefix, private_ip_address_allocation=private_ip_address_allocation, dns_name_for_public_ip=dns_name_for_public_ip, storage_account_type=storage_account_type, os_disk_uri=os_disk_uri, name=name, virtual_network_type=virtual_network_type, admin_password=admin_password, os_sku=os_sku, subnet_name=subnet_name, os_type=os_type, admin_username=admin_username, os_version=os_version, os_disk_name=os_disk_name, ssh_key_path=ssh_key_path, os_offer=os_offer, public_ip_address_allocation=public_ip_address_allocation, authentication_type=authentication_type, storage_account_name=storage_account_name, storage_redundancy_type=storage_redundancy_type, size=size, public_ip_address_type=public_ip_address_type, virtual_network_ip_address_prefix=virtual_network_ip_address_prefix, availability_set_id=availability_set_id, ssh_key_value=ssh_key_value, location=location, os_publisher=os_publisher, availability_set_type=availability_set_type, public_ip_address_name=public_ip_address_name, dns_name_type=dns_name_type)

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
        body_content = self._serialize.body(parameters, 'DeploymentVM')

        # Construct and send request
        def long_running_send():

            request = self._client.put(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers={}):

            request = self._client.get(status_link)
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
