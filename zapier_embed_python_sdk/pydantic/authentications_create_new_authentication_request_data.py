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


class AuthenticationsCreateNewAuthenticationRequestData(BaseModel):
    # The title of the authentication.
    title: str = Field(alias='title')

    # A canonical App ID, as provided by the `/apps` endpoint.
    app: str = Field(alias='app')

    # Required values to create an authentication. These values will be used by the target integration to successfully create the Authentication https://platform.zapier.com/build/auth.
    authentication_fields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='authentication_fields')
    class Config:
        arbitrary_types_allowed = True
