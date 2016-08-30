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


class ImportDevicesRequest(Model):
    """Used to provide parameters when requesting an import of all devices in the
    hub.

    :param input_blob_container_uri: The input BLOB container URI.
    :type input_blob_container_uri: str
    :param output_blob_container_uri: The output BLOB container URI.
    :type output_blob_container_uri: str
    """ 

    _validation = {
        'input_blob_container_uri': {'required': True},
        'output_blob_container_uri': {'required': True},
    }

    _attribute_map = {
        'input_blob_container_uri': {'key': 'InputBlobContainerUri', 'type': 'str'},
        'output_blob_container_uri': {'key': 'OutputBlobContainerUri', 'type': 'str'},
    }

    def __init__(self, input_blob_container_uri, output_blob_container_uri):
        self.input_blob_container_uri = input_blob_container_uri
        self.output_blob_container_uri = output_blob_container_uri
