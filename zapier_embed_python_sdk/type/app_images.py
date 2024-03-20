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


class RequiredAppImages(TypedDict):
    pass

class OptionalAppImages(TypedDict, total=False):
    url_16x16: str

    url_32x32: str

    url_64x64: str

    url_128x128: str

class AppImages(RequiredAppImages, OptionalAppImages):
    pass
