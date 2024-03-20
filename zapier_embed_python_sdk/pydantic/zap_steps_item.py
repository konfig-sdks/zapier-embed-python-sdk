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

from zapier_embed_python_sdk.pydantic.action import Action
from zapier_embed_python_sdk.pydantic.authentication import Authentication

class ZapStepsItem(BaseModel):
    # Expandable. The Action associated with this Zap step.
    action: typing.Union[str, Action] = Field(alias='action')

    inputs: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='inputs')

    # Expandable. The Authentication associated with this zap step.
    authentication: typing.Union[typing.Union[bool, date, datetime, dict, float, int, list, str, None], Authentication] = Field(alias='authentication')

    # The custom title of a Zap Step. If a step has not been given a custom title by the user, then the value will be null.
    title: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='title')
    class Config:
        arbitrary_types_allowed = True
