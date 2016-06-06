#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TemplateLink(Model):
    """
    Entity representing the reference to the template.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param content_version: If included it must match the ContentVersion in
     the template.
    :type content_version: str
    :ivar uri: URI referencing the template. Default value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreatePublicIp_2016-06-06/azuredeploy.json"
     .
    :vartype uri: str
    """ 

    _validation = {
        'uri': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'content_version': {'key': 'contentVersion', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
    }

    uri = "https://azuresdkci.blob.core.windows.net/templatehost/CreatePublicIp_2016-06-06/azuredeploy.json"

    def __init__(self, content_version=None):
        self.content_version = content_version
