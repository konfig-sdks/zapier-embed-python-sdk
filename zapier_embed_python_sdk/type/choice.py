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


class RequiredChoice(TypedDict):
    # The type of this object.
    type: str

    # The ID of this variant.
    id: str

    # The value of this variant.
    value: str

class OptionalChoice(TypedDict, total=False):
    # An optional human-readable label for this variant. Useful if the actual value is not a human-readable value, such as an identifier.
    label: str

class Choice(RequiredChoice, OptionalChoice):
    pass
