#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SubscriptionNotification(Model):
    """SubscriptionNotification

    :param registration_date:
    :type registration_date: datetime
    :param state: Possible values include: 'NotDefined', 'Registered',
     'Unregistered', 'Warned', 'Suspended', 'Deleted'
    :type state: str
    :param properties:
    :type properties: :class:`SubscriptionProperties
     <containerregistry.models.SubscriptionProperties>`
    """ 

    _attribute_map = {
        'registration_date': {'key': 'registrationDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'SubscriptionProperties'},
    }

    def __init__(self, registration_date=None, state=None, properties=None):
        self.registration_date = registration_date
        self.state = state
        self.properties = properties
