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

from zapier_embed_python_sdk.type.actions_get_input_fields_response_data import ActionsGetInputFieldsResponseData
from zapier_embed_python_sdk.type.meta import Meta

class RequiredActionsGetInputFieldsResponse(TypedDict):
    pass

class OptionalActionsGetInputFieldsResponse(TypedDict, total=False):
    meta: Meta

    data: ActionsGetInputFieldsResponseData

class ActionsGetInputFieldsResponse(RequiredActionsGetInputFieldsResponse, OptionalActionsGetInputFieldsResponse):
    pass
