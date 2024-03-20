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

from zapier_embed_python_sdk.pydantic.actions_get_input_fields_response_data import ActionsGetInputFieldsResponseData
from zapier_embed_python_sdk.pydantic.meta import Meta

class ActionsGetInputFieldsResponse(BaseModel):
    meta: typing.Optional[Meta] = Field(None, alias='meta')

    data: typing.Optional[ActionsGetInputFieldsResponseData] = Field(None, alias='data')
    class Config:
        arbitrary_types_allowed = True
