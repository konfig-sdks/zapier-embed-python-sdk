import typing_extensions

from zapier_embed_python_sdk.apis.tags import TagValues
from zapier_embed_python_sdk.apis.tags.actions_api import ActionsApi
from zapier_embed_python_sdk.apis.tags.authentications_api import AuthenticationsApi
from zapier_embed_python_sdk.apis.tags.zaps_api import ZapsApi
from zapier_embed_python_sdk.apis.tags.apps_api import AppsApi
from zapier_embed_python_sdk.apis.tags.experimental_api import ExperimentalApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACTIONS: ActionsApi,
        TagValues.AUTHENTICATIONS: AuthenticationsApi,
        TagValues.ZAPS: ZapsApi,
        TagValues.APPS: AppsApi,
        TagValues.EXPERIMENTAL: ExperimentalApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACTIONS: ActionsApi,
        TagValues.AUTHENTICATIONS: AuthenticationsApi,
        TagValues.ZAPS: ZapsApi,
        TagValues.APPS: AppsApi,
        TagValues.EXPERIMENTAL: ExperimentalApi,
    }
)
