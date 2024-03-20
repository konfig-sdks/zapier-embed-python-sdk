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
from pydantic import BaseModel, Field, RootModel

from zapier_embed_python_sdk.pydantic.input_field_depends_on import InputFieldDependsOn
from zapier_embed_python_sdk.pydantic.input_field_items import InputFieldItems

class InputField(BaseModel):
    # The title of this Input Field
    title: str = Field(alias='title')

    # A longer markdown formatted description of this Input Field, often containing helpful hints on how to fill this particular field in.
    description: str = Field(alias='description')

    # The type of this object.
    type: Literal["input_field", "info_field", "fieldset"] = Field(alias='type')

    id: str = Field(alias='id')

    # The default value of this Input Field
    default_value: str = Field(alias='default_value')

    depends_on: InputFieldDependsOn = Field(alias='depends_on')

    # If true, changes to this field invalidate the presence of all other fields for this action and they must be refetched.
    invalidates_input_fields: bool = Field(alias='invalidates_input_fields')

    # If true, this field must be filled in for the action to execute.
    is_required: bool = Field(alias='is_required')

    # A placeholder for this Input Field.
    placeholder: str = Field(alias='placeholder')

    # The type of this Input Field. The `OBJECT` type accepts a flat key-value dictionary where the values can only be strings. The `ARRAY` type accepts an array of values - see `items` for the type. All other types accept string values.
    value_type: Literal["STRING", "NUMBER", "INTEGER", "BOOLEAN", "ARRAY", "OBJECT"] = Field(alias='value_type')

    # An optional formatting hint, only provided when the `value_type` field is `STRING`. Useful for displaying more friendly inputs to a user. If the format is `SELECT`, you are expected to fetch the possible Choices from the `/choices` endpoint.
    format: typing.Optional[Literal["DATETIME", "MULTILINE", "PASSWORD", "CODE", "FILE", "SELECT"]] = Field(None, alias='format')

    items: typing.Optional[InputFieldItems] = Field(None, alias='items')
    class Config:
        arbitrary_types_allowed = True
