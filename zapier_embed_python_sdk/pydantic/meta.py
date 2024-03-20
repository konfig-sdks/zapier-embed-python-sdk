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


class Meta(BaseModel):
    # The limit value used in the request.
    limit: typing.Optional[int] = Field(None, alias='limit')

    # The offset value used in the request.
    offset: typing.Optional[int] = Field(None, alias='offset')

    # The total number of objects in the collection represented by the endpoint.
    count: typing.Optional[int] = Field(None, alias='count')
    class Config:
        arbitrary_types_allowed = True
