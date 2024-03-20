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

from zapier_embed_python_sdk.type.fieldset import Fieldset
from zapier_embed_python_sdk.type.info_field import InfoField
from zapier_embed_python_sdk.type.input_field import InputField

ActionsGetInputFieldsResponseData = typing.List[typing.Union[typing.List[InputField], typing.List[Fieldset], typing.List[InfoField]]]
