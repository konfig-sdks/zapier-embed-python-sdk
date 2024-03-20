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


class InputsWithAuthenticationIdNoPage(BaseModel):
    # An Authentication ID, as provided by the `/authentications` endpoint.
    authentication: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='authentication')

    # The current set of input fields in a JSON object, where each key is the `id` of an Input Field, and the corresponding value the current value of the field.
    inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='inputs')
    class Config:
        arbitrary_types_allowed = True
