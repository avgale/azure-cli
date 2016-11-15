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


class Contact(Model):
    """The contact information for the vault certificates.

    :param email_address: Email addresss.
    :type email_address: str
    :param name: Name.
    :type name: str
    :param phone: Phone number.
    :type phone: str
    """ 

    _attribute_map = {
        'email_address': {'key': 'email', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'phone': {'key': 'phone', 'type': 'str'},
    }

    def __init__(self, email_address=None, name=None, phone=None):
        self.email_address = email_address
        self.name = name
        self.phone = phone
