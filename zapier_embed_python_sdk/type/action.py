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

from zapier_embed_python_sdk.type.app import App

class RequiredAction(TypedDict):
    # The title of this Action.
    title: str

    # A longer description of this Action, usually describing what it does in more detail.
    description: str

    # The type of this object.
    type: str

    id: str

    # The developer provided identifier for this Action.
    key: str

    # The type of this Action.
    action_type: str

    # Expandable field for app.
    app: typing.Union[typing.Union[bool, date, datetime, dict, float, int, list, str, None], App]

    # Will be set to `true` if this Action triggers instantly. May only be `true` when `type` is `READ`.
    is_instant: bool

class OptionalAction(TypedDict, total=False):
    pass

class Action(RequiredAction, OptionalAction):
    pass
