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


class CertificatePolicy(Model):
    """Management policy for a certificate.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The certificate id
    :vartype id: str
    :param key_properties: Properties of the key backing a certificate.
    :type key_properties: :class:`KeyProperties
     <KeyVault.models.KeyProperties>`
    :param secret_properties: Properties of the secret backing a certificate.
    :type secret_properties: :class:`SecretProperties
     <KeyVault.models.SecretProperties>`
    :param x509_certificate_properties: Properties of the X509 component of a
     certificate.
    :type x509_certificate_properties: :class:`X509CertificateProperties
     <KeyVault.models.X509CertificateProperties>`
    :param lifetime_actions: Actions that will be performed by Key Vault over
     the lifetime of a certificate.
    :type lifetime_actions: list of :class:`LifetimeAction
     <KeyVault.models.LifetimeAction>`
    :param issuer_parameters: Parameters for the issuer of the X509 component
     of a certificate.
    :type issuer_parameters: :class:`IssuerParameters
     <KeyVault.models.IssuerParameters>`
    :param attributes: The certificate attributes.
    :type attributes: :class:`CertificateAttributes
     <KeyVault.models.CertificateAttributes>`
    """ 

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'key_properties': {'key': 'key_props', 'type': 'KeyProperties'},
        'secret_properties': {'key': 'secret_props', 'type': 'SecretProperties'},
        'x509_certificate_properties': {'key': 'x509_props', 'type': 'X509CertificateProperties'},
        'lifetime_actions': {'key': 'lifetime_actions', 'type': '[LifetimeAction]'},
        'issuer_parameters': {'key': 'issuer', 'type': 'IssuerParameters'},
        'attributes': {'key': 'attributes', 'type': 'CertificateAttributes'},
    }

    def __init__(self, key_properties=None, secret_properties=None, x509_certificate_properties=None, lifetime_actions=None, issuer_parameters=None, attributes=None):
        self.id = None
        self.key_properties = key_properties
        self.secret_properties = secret_properties
        self.x509_certificate_properties = x509_certificate_properties
        self.lifetime_actions = lifetime_actions
        self.issuer_parameters = issuer_parameters
        self.attributes = attributes
