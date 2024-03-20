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
from pydantic import BaseModel, Field, RootModel


class ZapLinks(BaseModel):
    # A link to open this Zap in the Zapier editor.
    html_editor: typing.Optional[str] = Field(None, alias='html_editor')
    class Config:
        arbitrary_types_allowed = True
