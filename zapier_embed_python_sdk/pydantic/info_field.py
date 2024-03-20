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


class InfoField(BaseModel):
    # A markdown formatted piece of text that provides helpful information to the user.
    description: str = Field(alias='description')

    # The type of this object.
    type: str = Field(alias='type')

    id: str = Field(alias='id')
    class Config:
        arbitrary_types_allowed = True