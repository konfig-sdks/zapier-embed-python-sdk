# coding: utf-8

# flake8: noqa

"""
    Zapier Embed API

    The Zapier Embed API.

    The version of the OpenAPI document: 1.0.0
    Contact: contact@zapier.com
    Created by: https://help.zapier.com/hc/en-us
"""

__version__ = "1.0.0"

# import ApiClient
from zapier_embed_python_sdk.api_client import ApiClient

# import Configuration
from zapier_embed_python_sdk.configuration import Configuration

# import exceptions
from zapier_embed_python_sdk.exceptions import OpenApiException
from zapier_embed_python_sdk.exceptions import ApiAttributeError
from zapier_embed_python_sdk.exceptions import ApiTypeError
from zapier_embed_python_sdk.exceptions import ApiValueError
from zapier_embed_python_sdk.exceptions import ApiKeyError
from zapier_embed_python_sdk.exceptions import ApiException

from zapier_embed_python_sdk.client import ZapierEmbed
