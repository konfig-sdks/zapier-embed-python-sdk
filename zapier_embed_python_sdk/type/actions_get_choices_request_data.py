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


class RequiredActionsGetChoicesRequestData(TypedDict):
    authentication: str

class OptionalActionsGetChoicesRequestData(TypedDict, total=False):
    inputs: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class ActionsGetChoicesRequestData(RequiredActionsGetChoicesRequestData, OptionalActionsGetChoicesRequestData):
    pass
