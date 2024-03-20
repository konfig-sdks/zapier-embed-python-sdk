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

from zapier_embed_python_sdk.type.actions_get_choices_request_data import ActionsGetChoicesRequestData

class RequiredActionsGetChoicesRequest(TypedDict):
    data: ActionsGetChoicesRequestData

class OptionalActionsGetChoicesRequest(TypedDict, total=False):
    pass

class ActionsGetChoicesRequest(RequiredActionsGetChoicesRequest, OptionalActionsGetChoicesRequest):
    pass
