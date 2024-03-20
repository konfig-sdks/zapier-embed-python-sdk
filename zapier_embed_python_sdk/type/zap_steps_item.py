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

from zapier_embed_python_sdk.type.action import Action
from zapier_embed_python_sdk.type.authentication import Authentication

class RequiredZapStepsItem(TypedDict):
    # Expandable. The Action associated with this Zap step.
    action: typing.Union[str, Action]

    inputs: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Expandable. The Authentication associated with this zap step.
    authentication: typing.Union[typing.Union[bool, date, datetime, dict, float, int, list, str, None], Authentication]

class OptionalZapStepsItem(TypedDict, total=False):
    # The custom title of a Zap Step. If a step has not been given a custom title by the user, then the value will be null.
    title: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class ZapStepsItem(RequiredZapStepsItem, OptionalZapStepsItem):
    pass
