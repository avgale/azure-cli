# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from .resource import Resource


class NotificationChannel(Resource):
    """A notification.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict
    :param web_hook_url: The webhook URL to send notifications to.
    :type web_hook_url: str
    :param description: Description of notification.
    :type description: str
    :param events: The list of event for which this notification is enabled.
    :type events: list of :class:`Event <devtestlabs.models.Event>`
    :ivar created_date: The creation date of the notification channel.
    :vartype created_date: datetime
    :param provisioning_state: The provisioning status of the resource.
    :type provisioning_state: str
    :param unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :type unique_identifier: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'web_hook_url': {'key': 'properties.webHookUrl', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'events': {'key': 'properties.events', 'type': '[Event]'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
    }

    def __init__(self, location=None, tags=None, web_hook_url=None, description=None, events=None, provisioning_state=None, unique_identifier=None):
        super(NotificationChannel, self).__init__(location=location, tags=tags)
        self.web_hook_url = web_hook_url
        self.description = description
        self.events = events
        self.created_date = None
        self.provisioning_state = provisioning_state
        self.unique_identifier = unique_identifier
