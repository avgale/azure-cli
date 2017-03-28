# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.paging import Paged


class GalleryImagePaged(Paged):
    """
    A paging container for iterating over a list of GalleryImage object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GalleryImage]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryImagePaged, self).__init__(*args, **kwargs)
