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


class RequiredInfoField(TypedDict):
    # A markdown formatted piece of text that provides helpful information to the user.
    description: str

    # The type of this object.
    type: str

    id: str

class OptionalInfoField(TypedDict, total=False):
    pass

class InfoField(RequiredInfoField, OptionalInfoField):
    pass
