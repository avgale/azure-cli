# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from .resource import Resource


class Schedule(Resource):
    """A schedule.

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
    :param status: The status of the schedule (i.e. Enabled, Disabled).
     Possible values include: 'Enabled', 'Disabled'
    :type status: str or :class:`EnableStatus
     <devtestlabs.models.EnableStatus>`
    :param task_type: The task type of the schedule (e.g. LabVmsShutdownTask,
     LabVmAutoStart).
    :type task_type: str
    :param weekly_recurrence: If the schedule will occur only some days of the
     week, specify the weekly recurrence.
    :type weekly_recurrence: :class:`WeekDetails
     <devtestlabs.models.WeekDetails>`
    :param daily_recurrence: If the schedule will occur once each day of the
     week, specify the daily recurrence.
    :type daily_recurrence: :class:`DayDetails
     <devtestlabs.models.DayDetails>`
    :param hourly_recurrence: If the schedule will occur multiple times a day,
     specify the hourly recurrence.
    :type hourly_recurrence: :class:`HourDetails
     <devtestlabs.models.HourDetails>`
    :param time_zone_id: The time zone ID (e.g. Pacific Standard time).
    :type time_zone_id: str
    :param notification_settings: Notification settings.
    :type notification_settings: :class:`NotificationSettings
     <devtestlabs.models.NotificationSettings>`
    :ivar created_date: The creation date of the schedule.
    :vartype created_date: datetime
    :param target_resource_id: The resource ID to which the schedule belongs
    :type target_resource_id: str
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
        'status': {'key': 'properties.status', 'type': 'str'},
        'task_type': {'key': 'properties.taskType', 'type': 'str'},
        'weekly_recurrence': {'key': 'properties.weeklyRecurrence', 'type': 'WeekDetails'},
        'daily_recurrence': {'key': 'properties.dailyRecurrence', 'type': 'DayDetails'},
        'hourly_recurrence': {'key': 'properties.hourlyRecurrence', 'type': 'HourDetails'},
        'time_zone_id': {'key': 'properties.timeZoneId', 'type': 'str'},
        'notification_settings': {'key': 'properties.notificationSettings', 'type': 'NotificationSettings'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'target_resource_id': {'key': 'properties.targetResourceId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
    }

    def __init__(self, location=None, tags=None, status=None, task_type=None, weekly_recurrence=None, daily_recurrence=None, hourly_recurrence=None, time_zone_id=None, notification_settings=None, target_resource_id=None, provisioning_state=None, unique_identifier=None):
        super(Schedule, self).__init__(location=location, tags=tags)
        self.status = status
        self.task_type = task_type
        self.weekly_recurrence = weekly_recurrence
        self.daily_recurrence = daily_recurrence
        self.hourly_recurrence = hourly_recurrence
        self.time_zone_id = time_zone_id
        self.notification_settings = notification_settings
        self.created_date = None
        self.target_resource_id = target_resource_id
        self.provisioning_state = provisioning_state
        self.unique_identifier = unique_identifier
