# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
#pylint: skip-file
from msrest.serialization import Model


class IssuerParameters(Model):
    """Parameters for the issuer of the X509 component of a certificate.

    :param name: Name of the referenced issuer object or reserved names e.g.
     'Self', 'Unknown'.
    :type name: str
    :param certificate_type: Type of certificate to be requested from the
     issuer provider.
    :type certificate_type: str
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'certificate_type': {'key': 'cty', 'type': 'str'},
    }

    def __init__(self, name=None, certificate_type=None):
        self.name = name
        self.certificate_type = certificate_type
