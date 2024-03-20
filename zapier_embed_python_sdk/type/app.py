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

from zapier_embed_python_sdk.type.app_categories import AppCategories
from zapier_embed_python_sdk.type.app_images import AppImages
from zapier_embed_python_sdk.type.app_links import AppLinks

class RequiredApp(TypedDict):
    # The type of this object.
    type: str

    # Unique id of the app
    id: str

class OptionalApp(TypedDict, total=False):
    # Human readable name of the app
    title: str

    # Human readable description of the app.
    description: str

    categories: AppCategories

    # A branded color that can be used to represent the app.
    hex_color: str

    # Default image/icon to represent the app.
    image: str

    images: AppImages

    links: AppLinks

class App(RequiredApp, OptionalApp):
    pass
