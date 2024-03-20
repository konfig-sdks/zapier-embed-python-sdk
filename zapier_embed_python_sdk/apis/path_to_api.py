import typing_extensions

from zapier_embed_python_sdk.paths import PathValues
from zapier_embed_python_sdk.apis.paths.actions import Actions
from zapier_embed_python_sdk.apis.paths.authentications import Authentications
from zapier_embed_python_sdk.apis.paths.actions_action_inputs import ActionsActionInputs
from zapier_embed_python_sdk.apis.paths.actions_action_outputs import ActionsActionOutputs
from zapier_embed_python_sdk.apis.paths.actions_action_inputs_input_choices import ActionsActionInputsInputChoices
from zapier_embed_python_sdk.apis.paths.apps import Apps
from zapier_embed_python_sdk.apis.paths.zap_runs import ZapRuns
from zapier_embed_python_sdk.apis.paths.zaps import Zaps
from zapier_embed_python_sdk.apis.paths.actions_action_test import ActionsActionTest

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACTIONS: Actions,
        PathValues.AUTHENTICATIONS: Authentications,
        PathValues.ACTIONS_ACTION_INPUTS: ActionsActionInputs,
        PathValues.ACTIONS_ACTION_OUTPUTS: ActionsActionOutputs,
        PathValues.ACTIONS_ACTION_INPUTS_INPUT_CHOICES: ActionsActionInputsInputChoices,
        PathValues.APPS: Apps,
        PathValues.ZAPRUNS: ZapRuns,
        PathValues.ZAPS: Zaps,
        PathValues.ACTIONS_ACTION_TEST: ActionsActionTest,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACTIONS: Actions,
        PathValues.AUTHENTICATIONS: Authentications,
        PathValues.ACTIONS_ACTION_INPUTS: ActionsActionInputs,
        PathValues.ACTIONS_ACTION_OUTPUTS: ActionsActionOutputs,
        PathValues.ACTIONS_ACTION_INPUTS_INPUT_CHOICES: ActionsActionInputsInputChoices,
        PathValues.APPS: Apps,
        PathValues.ZAPRUNS: ZapRuns,
        PathValues.ZAPS: Zaps,
        PathValues.ACTIONS_ACTION_TEST: ActionsActionTest,
    }
)
