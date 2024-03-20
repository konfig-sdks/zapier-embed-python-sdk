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


class RequiredInputFieldItems(TypedDict):
    pass

class OptionalInputFieldItems(TypedDict, total=False):
    # Only set when `type` is `ARRAY`. Specifies the `type` of the elements of the array.
    type: str

class InputFieldItems(RequiredInputFieldItems, OptionalInputFieldItems):
    pass
