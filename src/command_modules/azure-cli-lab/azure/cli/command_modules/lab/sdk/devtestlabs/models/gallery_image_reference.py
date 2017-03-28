# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class GalleryImageReference(Model):
    """The reference information for an Azure Marketplace image.

    :param offer: The offer of the gallery image.
    :type offer: str
    :param publisher: The publisher of the gallery image.
    :type publisher: str
    :param sku: The SKU of the gallery image.
    :type sku: str
    :param os_type: The OS type of the gallery image.
    :type os_type: str
    :param version: The version of the gallery image.
    :type version: str
    """

    _attribute_map = {
        'offer': {'key': 'offer', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
        'os_type': {'key': 'osType', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, offer=None, publisher=None, sku=None, os_type=None, version=None):
        self.offer = offer
        self.publisher = publisher
        self.sku = sku
        self.os_type = os_type
        self.version = version
