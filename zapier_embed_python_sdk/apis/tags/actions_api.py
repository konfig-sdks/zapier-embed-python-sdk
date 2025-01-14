# coding: utf-8

"""
    Zapier Embed API

    The Zapier Embed API.

    The version of the OpenAPI document: 1.0.0
    Contact: contact@zapier.com
    Created by: https://help.zapier.com/hc/en-us
"""

from zapier_embed_python_sdk.paths.actions_action_inputs_input_choices.post import GetChoices
from zapier_embed_python_sdk.paths.actions_action_inputs.post import GetInputFields
from zapier_embed_python_sdk.paths.actions_action_outputs.post import GetOutputFields
from zapier_embed_python_sdk.paths.actions.get import ListAvailableActions
from zapier_embed_python_sdk.paths.actions_action_test.post import TestActionExecution
from zapier_embed_python_sdk.apis.tags.actions_api_raw import ActionsApiRaw


class ActionsApi(
    GetChoices,
    GetInputFields,
    GetOutputFields,
    ListAvailableActions,
    TestActionExecution,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ActionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ActionsApiRaw(api_client)
