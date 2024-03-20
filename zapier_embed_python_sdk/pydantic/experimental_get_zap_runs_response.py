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

from zapier_embed_python_sdk.pydantic.links import Links
from zapier_embed_python_sdk.pydantic.meta import Meta
from zapier_embed_python_sdk.pydantic.zap_run import ZapRun

class ExperimentalGetZapRunsResponse(BaseModel):
    # The list of Zap Runs.
    data: typing.Optional[typing.List[ZapRun]] = Field(None, alias='data')

    links: typing.Optional[Links] = Field(None, alias='links')

    meta: typing.Optional[Meta] = Field(None, alias='Meta')
    class Config:
        arbitrary_types_allowed = True