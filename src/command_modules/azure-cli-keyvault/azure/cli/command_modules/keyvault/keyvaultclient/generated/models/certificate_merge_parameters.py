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


class CertificateMergeParameters(Model):
    """The certificate merge parameters.

    :param x509_certificates: The certificate or the certificate chain to
     merge
    :type x509_certificates: list of bytearray
    :param certificate_attributes: The attributes of the certificate
     (optional)
    :type certificate_attributes: :class:`CertificateAttributes
     <KeyVault.models.CertificateAttributes>`
    :param tags: Application-specific metadata in the form of key-value pairs
    :type tags: dict
    """ 

    _validation = {
        'x509_certificates': {'required': True},
    }

    _attribute_map = {
        'x509_certificates': {'key': 'x5c', 'type': '[bytearray]'},
        'certificate_attributes': {'key': 'attributes', 'type': 'CertificateAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, x509_certificates, certificate_attributes=None, tags=None):
        self.x509_certificates = x509_certificates
        self.certificate_attributes = certificate_attributes
        self.tags = tags
