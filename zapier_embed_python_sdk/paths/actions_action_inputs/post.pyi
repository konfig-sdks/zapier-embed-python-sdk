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
from zapier_embed_python_sdk.model.actions_get_input_fields_response import ActionsGetInputFieldsResponse as ActionsGetInputFieldsResponseSchema
from zapier_embed_python_sdk.model.actions_list_available_actions415_response import ActionsListAvailableActions415Response as ActionsListAvailableActions415ResponseSchema
from zapier_embed_python_sdk.model.actions_list_available_actions404_response import ActionsListAvailableActions404Response as ActionsListAvailableActions404ResponseSchema
from zapier_embed_python_sdk.model.actions_get_input_fields_request import ActionsGetInputFieldsRequest as ActionsGetInputFieldsRequestSchema
from zapier_embed_python_sdk.model.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse as ActionsListAvailableActionsdefaultResponseSchema
from zapier_embed_python_sdk.model.inputs_with_authentication_id import InputsWithAuthenticationId as InputsWithAuthenticationIdSchema

from zapier_embed_python_sdk.type.actions_list_available_actions404_response import ActionsListAvailableActions404Response
from zapier_embed_python_sdk.type.actions_get_input_fields_request import ActionsGetInputFieldsRequest
from zapier_embed_python_sdk.type.inputs_with_authentication_id import InputsWithAuthenticationId
from zapier_embed_python_sdk.type.actions_list_available_actions415_response import ActionsListAvailableActions415Response
from zapier_embed_python_sdk.type.actions_get_input_fields_response import ActionsGetInputFieldsResponse
from zapier_embed_python_sdk.type.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse
from zapier_embed_python_sdk.type.actions_list_available_actions406_response import ActionsListAvailableActions406Response

from ...api_client import Dictionary
from zapier_embed_python_sdk.pydantic.actions_get_input_fields_response import ActionsGetInputFieldsResponse as ActionsGetInputFieldsResponsePydantic
from zapier_embed_python_sdk.pydantic.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse as ActionsListAvailableActionsdefaultResponsePydantic
from zapier_embed_python_sdk.pydantic.actions_get_input_fields_request import ActionsGetInputFieldsRequest as ActionsGetInputFieldsRequestPydantic
from zapier_embed_python_sdk.pydantic.actions_list_available_actions404_response import ActionsListAvailableActions404Response as ActionsListAvailableActions404ResponsePydantic
from zapier_embed_python_sdk.pydantic.inputs_with_authentication_id import InputsWithAuthenticationId as InputsWithAuthenticationIdPydantic
from zapier_embed_python_sdk.pydantic.actions_list_available_actions406_response import ActionsListAvailableActions406Response as ActionsListAvailableActions406ResponsePydantic
from zapier_embed_python_sdk.pydantic.actions_list_available_actions415_response import ActionsListAvailableActions415Response as ActionsListAvailableActions415ResponsePydantic

# Path params
ActionSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'action': typing.Union[ActionSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_action = api_client.PathParameter(
    name="action",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ActionSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationVndApijson = ActionsGetInputFieldsRequestSchema


request_body_actions_get_input_fields_request = api_client.RequestBody(
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndApijson),
    },
)
SchemaFor200ResponseBodyApplicationVndApijson = ActionsGetInputFieldsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ActionsGetInputFieldsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ActionsGetInputFieldsResponse


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

    def _get_input_fields_mapped_args(
        self,
        action: str,
        data: typing.Optional[InputsWithAuthenticationId] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if data is not None:
            _body["data"] = data
        args.body = _body
        if action is not None:
            _path_params["action"] = action
        args.path = _path_params
        return args

    async def _aget_input_fields_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.api+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Input Fields
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_action,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/actions/{action}/inputs',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_actions_get_input_fields_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _get_input_fields_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.api+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Input Fields
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_action,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/actions/{action}/inputs',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_actions_get_input_fields_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class GetInputFieldsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_input_fields(
        self,
        action: str,
        data: typing.Optional[InputsWithAuthenticationId] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_input_fields_mapped_args(
            action=action,
            data=data,
        )
        return await self._aget_input_fields_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def get_input_fields(
        self,
        action: str,
        data: typing.Optional[InputsWithAuthenticationId] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_input_fields_mapped_args(
            action=action,
            data=data,
        )
        return self._get_input_fields_oapg(
            body=args.body,
            path_params=args.path,
        )

class GetInputFields(BaseApi):

    async def aget_input_fields(
        self,
        action: str,
        data: typing.Optional[InputsWithAuthenticationId] = None,
        validate: bool = False,
        **kwargs,
    ) -> ActionsGetInputFieldsResponsePydantic:
        raw_response = await self.raw.aget_input_fields(
            action=action,
            data=data,
            **kwargs,
        )
        if validate:
            return ActionsGetInputFieldsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ActionsGetInputFieldsResponsePydantic, raw_response.body)
    
    
    def get_input_fields(
        self,
        action: str,
        data: typing.Optional[InputsWithAuthenticationId] = None,
        validate: bool = False,
    ) -> ActionsGetInputFieldsResponsePydantic:
        raw_response = self.raw.get_input_fields(
            action=action,
            data=data,
        )
        if validate:
            return ActionsGetInputFieldsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ActionsGetInputFieldsResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        action: str,
        data: typing.Optional[InputsWithAuthenticationId] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_input_fields_mapped_args(
            action=action,
            data=data,
        )
        return await self._aget_input_fields_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        action: str,
        data: typing.Optional[InputsWithAuthenticationId] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_input_fields_mapped_args(
            action=action,
            data=data,
        )
        return self._get_input_fields_oapg(
            body=args.body,
            path_params=args.path,
        )

