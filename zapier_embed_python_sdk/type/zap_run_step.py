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


class RequiredZapRunStep(TypedDict):
    pass

class OptionalZapRunStep(TypedDict, total=False):
    # Represents the current state or progress of the Zap Run Step.
    status: str

    # The specific time when the execution of the step in the Zap run began.
    start_time: datetime

class ZapRunStep(RequiredZapRunStep, OptionalZapRunStep):
    pass
