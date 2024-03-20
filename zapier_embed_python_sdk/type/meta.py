# coding: utf-8

"""
    Zapier Embed API

    The Zapier Embed API.

    The version of the OpenAPI document: 1.0.0
    Contact: contact@zapier.com
    Created by: https://help.zapier.com/hc/en-us
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredMeta(TypedDict):
    pass

class OptionalMeta(TypedDict, total=False):
    # The limit value used in the request.
    limit: int

    # The offset value used in the request.
    offset: int

    # The total number of objects in the collection represented by the endpoint.
    count: int

class Meta(RequiredMeta, OptionalMeta):
    pass
