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

from zapier_embed_python_sdk.type.zap_run_step import ZapRunStep

class RequiredZapRun(TypedDict):
    pass

class OptionalZapRun(TypedDict, total=False):
    # Zap Run Identifier.
    id: str

    # The specific time when the Zap Run was initiated.
    start_time: datetime

    # The specific time when the Zap Run was finished.
    end_time: datetime

    # Represents the current state or progress of the Zap Run
    status: str

    # Refers to the name or title of the specific Zap that the run is associated with.
    zap_title: str

    # The list of sequential actions or processes involved in the execution of the associated Zap run.
    steps: typing.List[ZapRunStep]

    # The information about the data inputted into and logged out from a specific Zap Run during its execution.
    data_in: str

    # The information logged out from a specific Zap Run during its execution.
    data_out: str

class ZapRun(RequiredZapRun, OptionalZapRun):
    pass
