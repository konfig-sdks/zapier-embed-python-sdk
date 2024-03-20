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

from zapier_embed_python_sdk.pydantic.zap_links import ZapLinks
from zapier_embed_python_sdk.pydantic.zap_steps import ZapSteps

class Zap(BaseModel):
    # The human readable name of the Zap.
    title: str = Field(alias='title')

    steps: ZapSteps = Field(alias='steps')

    # The type of this object.
    type: typing.Optional[str] = Field(None, alias='type')

    # A unique identifier of the Zap.
    id: typing.Optional[str] = Field(None, alias='id')

    # Whether the Zap is enabled (running) or not.
    is_enabled: typing.Optional[bool] = Field(None, alias='is_enabled')

    # The date/time at which this Zap last ran sucessfully. A null value indicates that a Zap has never run successfully.
    last_successful_run_date: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='last_successful_run_date')

    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')

    links: typing.Optional[ZapLinks] = Field(None, alias='links')
    class Config:
        arbitrary_types_allowed = True
