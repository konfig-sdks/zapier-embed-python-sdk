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


class RequiredOutputField(TypedDict):
    # The title of this Output Field
    title: str

    # The type of this object.
    type: str

    id: str

class OptionalOutputField(TypedDict, total=False):
    # An optional sample of the data this Output Field might contain.
    sample: str

class OutputField(RequiredOutputField, OptionalOutputField):
    pass
