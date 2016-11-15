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

from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_operation import AzureOperationPoller
import uuid

from .. import models


class PublicIpOperations(object):
    """PublicIpOperations operations.

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
            self, resource_group_name, deployment_name, name, content_version=None, allocation_method="dynamic", dns_name=None, dns_name_type="none", idle_timeout=4, location=None, reverse_fqdn=None, tags=None, version="ipv4", custom_headers=None, raw=False, **operation_config):
        """
        Create a new PublicIp.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param deployment_name: The name of the deployment.
        :type deployment_name: str
        :param name: Name of the Public IP address.
        :type name: str
        :param content_version: If included it must match the ContentVersion
         in the template.
        :type content_version: str
        :param allocation_method: IP address Allocation method. Possible
         values include: 'dynamic', 'static'
        :type allocation_method: str or :class:`allocationMethod
         <publicipcreationclient.models.allocationMethod>`
        :param dns_name: Globally unique DNS entry.
        :type dns_name: str
        :param dns_name_type: Whether to include a DNS entry or not. Possible
         values include: 'new', 'none'
        :type dns_name_type: str or :class:`dnsNameType
         <publicipcreationclient.models.dnsNameType>`
        :param idle_timeout: Idle timeout in minutes.
        :type idle_timeout: int
        :param location: Location (e.g. eastus).
        :type location: str
        :param reverse_fqdn: Reverse FQDN (fully qualified domain name).
        :type reverse_fqdn: str
        :param tags: Tags object.
        :type tags: object
        :param version: IP address type. Possible values include: 'ipv4',
         'ipv6'
        :type version: str or :class:`version
         <publicipcreationclient.models.version>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`DeploymentExtended
         <default.models.DeploymentExtended>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        parameters = models.DeploymentPublicIp(content_version=content_version, allocation_method=allocation_method, dns_name=dns_name, dns_name_type=dns_name_type, idle_timeout=idle_timeout, location=location, name=name, reverse_fqdn=reverse_fqdn, tags=tags, version=version)

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
        body_content = self._serialize.body(parameters, 'DeploymentPublicIp')

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
