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

from zapier_embed_python_sdk.type.json_error import JSONError

class RequiredZapsGetFilteredZaps401Response(TypedDict):
    pass

class OptionalZapsGetFilteredZaps401Response(TypedDict, total=False):
    errors: typing.List[JSONError]

class ZapsGetFilteredZaps401Response(RequiredZapsGetFilteredZaps401Response, OptionalZapsGetFilteredZaps401Response):
    pass
