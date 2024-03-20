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

class Action(BaseModel):
    # The title of this Action.
    title: str = Field(alias='title')

    # A longer description of this Action, usually describing what it does in more detail.
    description: str = Field(alias='description')

    # The type of this object.
    type: str = Field(alias='type')

    id: str = Field(alias='id')

    # The developer provided identifier for this Action.
    key: str = Field(alias='key')

    # The type of this Action.
    action_type: Literal["READ", "WRITE"] = Field(alias='action_type')

    # Expandable field for app.
    app: typing.Union[typing.Union[bool, date, datetime, dict, float, int, list, str, None], App] = Field(alias='app')

    # Will be set to `true` if this Action triggers instantly. May only be `true` when `type` is `READ`.
    is_instant: bool = Field(alias='is_instant')
    class Config:
        arbitrary_types_allowed = True
