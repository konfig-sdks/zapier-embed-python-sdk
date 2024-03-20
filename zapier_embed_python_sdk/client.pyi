# coding: utf-8
"""
    Zapier Embed API

    The Zapier Embed API.

    The version of the OpenAPI document: 1.0.0
    Contact: contact@zapier.com
    Created by: https://help.zapier.com/hc/en-us
"""

import typing
import inspect
from datetime import date, datetime
from zapier_embed_python_sdk.client_custom import ClientCustom
from zapier_embed_python_sdk.configuration import Configuration
from zapier_embed_python_sdk.api_client import ApiClient
from zapier_embed_python_sdk.type_util import copy_signature
from zapier_embed_python_sdk.apis.tags.actions_api import ActionsApi
from zapier_embed_python_sdk.apis.tags.apps_api import AppsApi
from zapier_embed_python_sdk.apis.tags.authentications_api import AuthenticationsApi
from zapier_embed_python_sdk.apis.tags.experimental_api import ExperimentalApi
from zapier_embed_python_sdk.apis.tags.zaps_api import ZapsApi



class ZapierEmbed(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.actions: ActionsApi = ActionsApi(api_client)
        self.apps: AppsApi = AppsApi(api_client)
        self.authentications: AuthenticationsApi = AuthenticationsApi(api_client)
        self.experimental: ExperimentalApi = ExperimentalApi(api_client)
        self.zaps: ZapsApi = ZapsApi(api_client)
