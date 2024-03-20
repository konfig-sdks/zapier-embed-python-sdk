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
from zapier_embed_python_sdk.type.zap import Zap

class RequiredZapsGetFilteredZapsResponse(TypedDict):
    pass

class OptionalZapsGetFilteredZapsResponse(TypedDict, total=False):
    links: Links

    meta: Meta

    data: typing.List[Zap]

class ZapsGetFilteredZapsResponse(RequiredZapsGetFilteredZapsResponse, OptionalZapsGetFilteredZapsResponse):
    pass
