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


class ZapRunStep(BaseModel):
    # Represents the current state or progress of the Zap Run Step.
    status: typing.Optional[Literal["delayed", "scheduled", "pending", "error", "halted", "throttled", "held", "filtered", "skipped", "success"]] = Field(None, alias='status')

    # The specific time when the execution of the step in the Zap run began.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')
    class Config:
        arbitrary_types_allowed = True
