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

from zapier_embed_python_sdk.type.zap_links import ZapLinks
from zapier_embed_python_sdk.type.zap_steps import ZapSteps

class RequiredZap(TypedDict):
    # The human readable name of the Zap.
    title: str

    steps: ZapSteps

class OptionalZap(TypedDict, total=False):
    # The type of this object.
    type: str

    # A unique identifier of the Zap.
    id: str

    # Whether the Zap is enabled (running) or not.
    is_enabled: bool

    # The date/time at which this Zap last ran sucessfully. A null value indicates that a Zap has never run successfully.
    last_successful_run_date: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    updated_at: datetime

    links: ZapLinks

class Zap(RequiredZap, OptionalZap):
    pass
