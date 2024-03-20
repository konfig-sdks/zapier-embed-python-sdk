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


class RequiredLinksWithPage(TypedDict):
    pass

class OptionalLinksWithPage(TypedDict, total=False):
    # The URL of the next page of paginated results.
    next: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The URL of the previous page of paginated results.
    prev: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class LinksWithPage(RequiredLinksWithPage, OptionalLinksWithPage):
    pass
