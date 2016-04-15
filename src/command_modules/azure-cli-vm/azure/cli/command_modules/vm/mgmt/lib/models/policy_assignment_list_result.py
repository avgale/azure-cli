#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.15.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PolicyAssignmentListResult(Model):
    """
    Policy assignment list operation result.

    :param list value: Policy assignment list.
    :param str next_link: Gets or sets the URL to get the next set of policy
     assignment results.
    """ 

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicyAssignment]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, value=None, next_link=None, **kwargs):
        self.value = value
        self.next_link = next_link
