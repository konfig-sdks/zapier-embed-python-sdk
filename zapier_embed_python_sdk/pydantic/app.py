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

from zapier_embed_python_sdk.pydantic.app_categories import AppCategories
from zapier_embed_python_sdk.pydantic.app_images import AppImages
from zapier_embed_python_sdk.pydantic.app_links import AppLinks

class App(BaseModel):
    # The type of this object.
    type: str = Field(alias='type')

    # Unique id of the app
    id: str = Field(alias='id')

    # Human readable name of the app
    title: typing.Optional[str] = Field(None, alias='title')

    # Human readable description of the app.
    description: typing.Optional[str] = Field(None, alias='description')

    categories: typing.Optional[AppCategories] = Field(None, alias='categories')

    # A branded color that can be used to represent the app.
    hex_color: typing.Optional[str] = Field(None, alias='hex_color')

    # Default image/icon to represent the app.
    image: typing.Optional[str] = Field(None, alias='image')

    images: typing.Optional[AppImages] = Field(None, alias='images')

    links: typing.Optional[AppLinks] = Field(None, alias='links')
    class Config:
        arbitrary_types_allowed = True
