# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class GenerateUploadUriResponse(Model):
    """Reponse body for generating an upload URI.

    :param upload_uri: The upload URI for the VHD.
    :type upload_uri: str
    """

    _attribute_map = {
        'upload_uri': {'key': 'uploadUri', 'type': 'str'},
    }

    def __init__(self, upload_uri=None):
        self.upload_uri = upload_uri
