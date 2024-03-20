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

from zapier_embed_python_sdk.type.fieldset_fields import FieldsetFields

class RequiredFieldset(TypedDict):
    # The human readable title for this group of fields.
    title: str

    # The type of this object.
    type: str

    id: str

    fields: FieldsetFields

class OptionalFieldset(TypedDict, total=False):
    pass

class Fieldset(RequiredFieldset, OptionalFieldset):
    pass
