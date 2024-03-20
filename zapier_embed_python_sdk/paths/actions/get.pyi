# coding: utf-8

"""
    Zapier Embed API

    The Zapier Embed API.

    The version of the OpenAPI document: 1.0.0
    Contact: contact@zapier.com
    Created by: https://help.zapier.com/hc/en-us
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from zapier_embed_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from zapier_embed_python_sdk.api_response import AsyncGeneratorResponse
from zapier_embed_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from zapier_embed_python_sdk import schemas  # noqa: F401

from zapier_embed_python_sdk.model.actions_list_available_actions406_response import ActionsListAvailableActions406Response as ActionsListAvailableActions406ResponseSchema
from zapier_embed_python_sdk.model.actions_list_available_actions415_response import ActionsListAvailableActions415Response as ActionsListAvailableActions415ResponseSchema
from zapier_embed_python_sdk.model.actions_list_available_actions404_response import ActionsListAvailableActions404Response as ActionsListAvailableActions404ResponseSchema
from zapier_embed_python_sdk.model.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse as ActionsListAvailableActionsdefaultResponseSchema
from zapier_embed_python_sdk.model.actions_list_available_actions_response import ActionsListAvailableActionsResponse as ActionsListAvailableActionsResponseSchema

from zapier_embed_python_sdk.type.actions_list_available_actions404_response import ActionsListAvailableActions404Response
from zapier_embed_python_sdk.type.actions_list_available_actions_response import ActionsListAvailableActionsResponse
from zapier_embed_python_sdk.type.actions_list_available_actions415_response import ActionsListAvailableActions415Response
from zapier_embed_python_sdk.type.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse
from zapier_embed_python_sdk.type.actions_list_available_actions406_response import ActionsListAvailableActions406Response

from ...api_client import Dictionary
from zapier_embed_python_sdk.pydantic.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse as ActionsListAvailableActionsdefaultResponsePydantic
from zapier_embed_python_sdk.pydantic.actions_list_available_actions_response import ActionsListAvailableActionsResponse as ActionsListAvailableActionsResponsePydantic
from zapier_embed_python_sdk.pydantic.actions_list_available_actions404_response import ActionsListAvailableActions404Response as ActionsListAvailableActions404ResponsePydantic
from zapier_embed_python_sdk.pydantic.actions_list_available_actions406_response import ActionsListAvailableActions406Response as ActionsListAvailableActions406ResponsePydantic
from zapier_embed_python_sdk.pydantic.actions_list_available_actions415_response import ActionsListAvailableActions415Response as ActionsListAvailableActions415ResponsePydantic

# Query params
AppSchema = schemas.UUIDSchema


class ActionTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def READ(cls):
        return cls("READ")
    
    @schemas.classproperty
    def WRITE(cls):
        return cls("WRITE")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'app': typing.Union[AppSchema, str, uuid.UUID, ],
        'action_type': typing.Union[ActionTypeSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_app = api_client.QueryParameter(
    name="app",
    style=api_client.ParameterStyle.FORM,
    schema=AppSchema,
    required=True,
    explode=True,
)
request_query_action_type = api_client.QueryParameter(
    name="action_type",
    style=api_client.ParameterStyle.FORM,
    schema=ActionTypeSchema,
    required=True,
    explode=True,
)
SchemaFor200ResponseBodyApplicationVndApijson = ActionsListAvailableActionsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ActionsListAvailableActionsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ActionsListAvailableActionsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndApijson),
    },
)
SchemaFor404ResponseBodyApplicationVndApijson = ActionsListAvailableActions404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ActionsListAvailableActions404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ActionsListAvailableActions404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndApijson),
    },
)
SchemaFor406ResponseBodyApplicationVndApijson = ActionsListAvailableActions406ResponseSchema


@dataclass
class ApiResponseFor406(api_client.ApiResponse):
    body: ActionsListAvailableActions406Response


@dataclass
class ApiResponseFor406Async(api_client.AsyncApiResponse):
    body: ActionsListAvailableActions406Response


_response_for_406 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor406,
    response_cls_async=ApiResponseFor406Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor406ResponseBodyApplicationVndApijson),
    },
)
SchemaFor415ResponseBodyApplicationVndApijson = ActionsListAvailableActions415ResponseSchema


@dataclass
class ApiResponseFor415(api_client.ApiResponse):
    body: ActionsListAvailableActions415Response


@dataclass
class ApiResponseFor415Async(api_client.AsyncApiResponse):
    body: ActionsListAvailableActions415Response


_response_for_415 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor415,
    response_cls_async=ApiResponseFor415Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor415ResponseBodyApplicationVndApijson),
    },
)
SchemaFor0ResponseBodyApplicationVndApijson = ActionsListAvailableActionsdefaultResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ActionsListAvailableActionsdefaultResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ActionsListAvailableActionsdefaultResponse


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationVndApijson),
    },
)
_all_accept_content_types = (
    'application/vnd.api+json',
)


class BaseApi(api_client.Api):

    def _list_available_actions_mapped_args(
        self,
        app: str,
        action_type: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if app is not None:
            _query_params["app"] = app
        if action_type is not None:
            _query_params["action_type"] = action_type
        args.query = _query_params
        return args

    async def _alist_available_actions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Actions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_app,
            request_query_action_type,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/actions',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_available_actions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Actions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_app,
            request_query_action_type,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/actions',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListAvailableActionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_available_actions(
        self,
        app: str,
        action_type: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_available_actions_mapped_args(
            app=app,
            action_type=action_type,
        )
        return await self._alist_available_actions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_available_actions(
        self,
        app: str,
        action_type: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_available_actions_mapped_args(
            app=app,
            action_type=action_type,
        )
        return self._list_available_actions_oapg(
            query_params=args.query,
        )

class ListAvailableActions(BaseApi):

    async def alist_available_actions(
        self,
        app: str,
        action_type: str,
        validate: bool = False,
        **kwargs,
    ) -> ActionsListAvailableActionsResponsePydantic:
        raw_response = await self.raw.alist_available_actions(
            app=app,
            action_type=action_type,
            **kwargs,
        )
        if validate:
            return ActionsListAvailableActionsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ActionsListAvailableActionsResponsePydantic, raw_response.body)
    
    
    def list_available_actions(
        self,
        app: str,
        action_type: str,
        validate: bool = False,
    ) -> ActionsListAvailableActionsResponsePydantic:
        raw_response = self.raw.list_available_actions(
            app=app,
            action_type=action_type,
        )
        if validate:
            return ActionsListAvailableActionsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ActionsListAvailableActionsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        app: str,
        action_type: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_available_actions_mapped_args(
            app=app,
            action_type=action_type,
        )
        return await self._alist_available_actions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        app: str,
        action_type: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_available_actions_mapped_args(
            app=app,
            action_type=action_type,
        )
        return self._list_available_actions_oapg(
            query_params=args.query,
        )

