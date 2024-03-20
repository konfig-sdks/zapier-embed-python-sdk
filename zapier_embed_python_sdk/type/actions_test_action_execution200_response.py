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

from zapier_embed_python_sdk.type.actions_test_action_execution200_response_data import ActionsTestActionExecution200ResponseData
from zapier_embed_python_sdk.type.links import Links
from zapier_embed_python_sdk.type.meta import Meta

class RequiredActionsTestActionExecution200Response(TypedDict):
    pass

class OptionalActionsTestActionExecution200Response(TypedDict, total=False):
    data: ActionsTestActionExecution200ResponseData

    meta: Meta

    links: Links

class ActionsTestActionExecution200Response(RequiredActionsTestActionExecution200Response, OptionalActionsTestActionExecution200Response):
    pass
