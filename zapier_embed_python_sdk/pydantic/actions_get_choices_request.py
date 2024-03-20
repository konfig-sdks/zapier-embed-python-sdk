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

from zapier_embed_python_sdk.pydantic.actions_get_choices_request_data import ActionsGetChoicesRequestData

class ActionsGetChoicesRequest(BaseModel):
    data: ActionsGetChoicesRequestData = Field(alias='data')
    class Config:
        arbitrary_types_allowed = True
