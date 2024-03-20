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

class RequiredAuthentication(TypedDict):
    title: str

    # The type of this object.
    type: str

    id: str

    app: typing.Union[str, App]

    # If `true`, this Authentication has expired. It will not be usable, and the user needs to be directed to reconnect it.
    is_expired: bool

class OptionalAuthentication(TypedDict, total=False):
    pass

class Authentication(RequiredAuthentication, OptionalAuthentication):
    pass
