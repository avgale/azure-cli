#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
#pylint: skip-file
from msrest.serialization import Model


class X509CertificateProperties(Model):
    """Properties of the X509 component of a certificate.

    :param subject: The subject name. Should be a valid X509 Distinguished
     Name.
    :type subject: str
    :param ekus: The enhanced key usage.
    :type ekus: list of str
    :param subject_alternative_names: The subject alternative names.
    :type subject_alternative_names: :class:`SubjectAlternativeNames
     <KeyVault.models.SubjectAlternativeNames>`
    :param key_usage: List of key usages.
    :type key_usage: list of str or :class:`KeyUsageType
     <KeyVault.models.KeyUsageType>`
    :param validity_in_months: The duration that the ceritifcate is valid in
     months.
    :type validity_in_months: int
    """ 

    _validation = {
        'validity_in_months': {'minimum': 0},
    }

    _attribute_map = {
        'subject': {'key': 'subject', 'type': 'str'},
        'ekus': {'key': 'ekus', 'type': '[str]'},
        'subject_alternative_names': {'key': 'sans', 'type': 'SubjectAlternativeNames'},
        'key_usage': {'key': 'key_usage', 'type': '[KeyUsageType]'},
        'validity_in_months': {'key': 'validity_months', 'type': 'int'},
    }

    def __init__(self, subject=None, ekus=None, subject_alternative_names=None, key_usage=None, validity_in_months=None):
        self.subject = subject
        self.ekus = ekus
        self.subject_alternative_names = subject_alternative_names
        self.key_usage = key_usage
        self.validity_in_months = validity_in_months
