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

from zapier_embed_python_sdk.pydantic.zap_run_step import ZapRunStep

class ZapRun(BaseModel):
    # Zap Run Identifier.
    id: typing.Optional[str] = Field(None, alias='id')

    # The specific time when the Zap Run was initiated.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The specific time when the Zap Run was finished.
    end_time: typing.Optional[datetime] = Field(None, alias='end_time')

    # Represents the current state or progress of the Zap Run
    status: typing.Optional[Literal["delayed", "scheduled", "pending", "error", "halted", "throttled", "held", "filtered", "skipped", "success"]] = Field(None, alias='status')

    # Refers to the name or title of the specific Zap that the run is associated with.
    zap_title: typing.Optional[str] = Field(None, alias='zap_title')

    # The list of sequential actions or processes involved in the execution of the associated Zap run.
    steps: typing.Optional[typing.List[ZapRunStep]] = Field(None, alias='steps')

    # The information about the data inputted into and logged out from a specific Zap Run during its execution.
    data_in: typing.Optional[str] = Field(None, alias='data_in')

    # The information logged out from a specific Zap Run during its execution.
    data_out: typing.Optional[str] = Field(None, alias='data_out')
    class Config:
        arbitrary_types_allowed = True
