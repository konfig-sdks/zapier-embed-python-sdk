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


class AppLinks(BaseModel):
    # A url that, when visited, will direct the user to authenticate with the app and allow Zapier access to the app, thus creating a new Authentication.  If value is `null`, then no authentication is required to use the app.
    connect_new_authentication: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='connect_new_authentication')
    class Config:
        arbitrary_types_allowed = True
