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


class OutputField(BaseModel):
    # The title of this Output Field
    title: str = Field(alias='title')

    # The type of this object.
    type: str = Field(alias='type')

    id: str = Field(alias='id')

    # An optional sample of the data this Output Field might contain.
    sample: typing.Optional[str] = Field(None, alias='sample')
    class Config:
        arbitrary_types_allowed = True
