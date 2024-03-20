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

from zapier_embed_python_sdk.pydantic.json_error import JSONError

class ActionsListAvailableActionsdefaultResponse(BaseModel):
    errors: typing.Optional[typing.List[JSONError]] = Field(None, alias='errors')
    class Config:
        arbitrary_types_allowed = True
