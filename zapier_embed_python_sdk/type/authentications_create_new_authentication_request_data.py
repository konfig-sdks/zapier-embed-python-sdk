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


class RequiredAuthenticationsCreateNewAuthenticationRequestData(TypedDict):
    # The title of the authentication.
    title: str

    # A canonical App ID, as provided by the `/apps` endpoint.
    app: str

    # Required values to create an authentication. These values will be used by the target integration to successfully create the Authentication https://platform.zapier.com/build/auth.
    authentication_fields: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalAuthenticationsCreateNewAuthenticationRequestData(TypedDict, total=False):
    pass

class AuthenticationsCreateNewAuthenticationRequestData(RequiredAuthenticationsCreateNewAuthenticationRequestData, OptionalAuthenticationsCreateNewAuthenticationRequestData):
    pass
