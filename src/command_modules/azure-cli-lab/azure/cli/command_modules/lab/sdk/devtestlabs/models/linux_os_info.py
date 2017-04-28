# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class LinuxOsInfo(Model):
    """Information about a Linux OS.

    :param linux_os_state: The state of the Linux OS (i.e. NonDeprovisioned,
     DeprovisionRequested, DeprovisionApplied). Possible values include:
     'NonDeprovisioned', 'DeprovisionRequested', 'DeprovisionApplied'
    :type linux_os_state: str or :class:`LinuxOsState
     <devtestlabs.models.LinuxOsState>`
    """

    _attribute_map = {
        'linux_os_state': {'key': 'linuxOsState', 'type': 'str'},
    }

    def __init__(self, linux_os_state=None):
        self.linux_os_state = linux_os_state
