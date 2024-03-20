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

from zapier_embed_python_sdk.pydantic.app import App

class Authentication(BaseModel):
    title: str = Field(alias='title')

    # The type of this object.
    type: str = Field(alias='type')

    id: str = Field(alias='id')

    app: typing.Union[str, App] = Field(alias='app')

    # If `true`, this Authentication has expired. It will not be usable, and the user needs to be directed to reconnect it.
    is_expired: bool = Field(alias='is_expired')
    class Config:
        arbitrary_types_allowed = True