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

from zapier_embed_python_sdk.type.links import Links
from zapier_embed_python_sdk.type.meta import Meta
from zapier_embed_python_sdk.type.zap_run import ZapRun

class RequiredExperimentalGetZapRunsResponse(TypedDict):
    pass

class OptionalExperimentalGetZapRunsResponse(TypedDict, total=False):
    # The list of Zap Runs.
    data: typing.List[ZapRun]

    links: Links

    Meta: Meta

class ExperimentalGetZapRunsResponse(RequiredExperimentalGetZapRunsResponse, OptionalExperimentalGetZapRunsResponse):
    pass
