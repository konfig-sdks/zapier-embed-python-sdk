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
from zapier_embed_python_sdk.type.links import Links
from zapier_embed_python_sdk.type.meta import Meta

class RequiredActionsListAvailableActionsResponse(TypedDict):
    pass

class OptionalActionsListAvailableActionsResponse(TypedDict, total=False):
    links: Links

    meta: Meta

    data: typing.List[Action]

class ActionsListAvailableActionsResponse(RequiredActionsListAvailableActionsResponse, OptionalActionsListAvailableActionsResponse):
    pass
