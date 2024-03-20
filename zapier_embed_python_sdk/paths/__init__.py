# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from zapier_embed_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACTIONS = "/actions"
    AUTHENTICATIONS = "/authentications"
    ACTIONS_ACTION_INPUTS = "/actions/{action}/inputs"
    ACTIONS_ACTION_OUTPUTS = "/actions/{action}/outputs"
    ACTIONS_ACTION_INPUTS_INPUT_CHOICES = "/actions/{action}/inputs/{input}/choices"
    APPS = "/apps"
    ZAPRUNS = "/zap-runs"
    ZAPS = "/zaps"
    ACTIONS_ACTION_TEST = "/actions/{action}/test"
