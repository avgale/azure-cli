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


class X509Thumbprint(Model):
    """X509Thumbprint.

    :param primary_thumbprint: The primary thumbprint.
    :type primary_thumbprint: str
    :param secondary_thumbprint: The secondary thumbprint.
    :type secondary_thumbprint: str
    """ 

    _attribute_map = {
        'primary_thumbprint': {'key': 'primaryThumbprint', 'type': 'str'},
        'secondary_thumbprint': {'key': 'secondaryThumbprint', 'type': 'str'},
    }

    def __init__(self, primary_thumbprint=None, secondary_thumbprint=None):
        self.primary_thumbprint = primary_thumbprint
        self.secondary_thumbprint = secondary_thumbprint
