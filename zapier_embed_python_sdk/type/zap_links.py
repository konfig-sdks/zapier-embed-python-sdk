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


class RequiredZapLinks(TypedDict):
    pass

class OptionalZapLinks(TypedDict, total=False):
    # A link to open this Zap in the Zapier editor.
    html_editor: str

class ZapLinks(RequiredZapLinks, OptionalZapLinks):
    pass
