# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class DetachDiskProperties(Model):
    """Properties of the disk to detach.

    :param leased_by_lab_vm_id: The resource ID of the Lab VM to which the
     disk is attached.
    :type leased_by_lab_vm_id: str
    """

    _attribute_map = {
        'leased_by_lab_vm_id': {'key': 'leasedByLabVmId', 'type': 'str'},
    }

    def __init__(self, leased_by_lab_vm_id=None):
        self.leased_by_lab_vm_id = leased_by_lab_vm_id
