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

from zapier_embed_python_sdk.type.input_field_depends_on import InputFieldDependsOn
from zapier_embed_python_sdk.type.input_field_items import InputFieldItems

class RequiredInputField(TypedDict):
    # The title of this Input Field
    title: str

    # A longer markdown formatted description of this Input Field, often containing helpful hints on how to fill this particular field in.
    description: str

    # The type of this object.
    type: str

    id: str

    # The default value of this Input Field
    default_value: str

    depends_on: InputFieldDependsOn

    # If true, changes to this field invalidate the presence of all other fields for this action and they must be refetched.
    invalidates_input_fields: bool

    # If true, this field must be filled in for the action to execute.
    is_required: bool

    # A placeholder for this Input Field.
    placeholder: str

    # The type of this Input Field. The `OBJECT` type accepts a flat key-value dictionary where the values can only be strings. The `ARRAY` type accepts an array of values - see `items` for the type. All other types accept string values.
    value_type: str

class OptionalInputField(TypedDict, total=False):
    # An optional formatting hint, only provided when the `value_type` field is `STRING`. Useful for displaying more friendly inputs to a user. If the format is `SELECT`, you are expected to fetch the possible Choices from the `/choices` endpoint.
    format: str

    items: InputFieldItems

class InputField(RequiredInputField, OptionalInputField):
    pass
