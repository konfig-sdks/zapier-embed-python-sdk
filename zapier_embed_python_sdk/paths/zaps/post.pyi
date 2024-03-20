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

from zapier_embed_python_sdk.model.zaps_create_zap_request import ZapsCreateZapRequest as ZapsCreateZapRequestSchema
from zapier_embed_python_sdk.model.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse as ActionsListAvailableActionsdefaultResponseSchema
from zapier_embed_python_sdk.model.zap import Zap as ZapSchema
from zapier_embed_python_sdk.model.zaps_create_zap_response import ZapsCreateZapResponse as ZapsCreateZapResponseSchema

from zapier_embed_python_sdk.type.zap import Zap
from zapier_embed_python_sdk.type.zaps_create_zap_response import ZapsCreateZapResponse
from zapier_embed_python_sdk.type.zaps_create_zap_request import ZapsCreateZapRequest
from zapier_embed_python_sdk.type.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse

from ...api_client import Dictionary
from zapier_embed_python_sdk.pydantic.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse as ActionsListAvailableActionsdefaultResponsePydantic
from zapier_embed_python_sdk.pydantic.zaps_create_zap_response import ZapsCreateZapResponse as ZapsCreateZapResponsePydantic
from zapier_embed_python_sdk.pydantic.zaps_create_zap_request import ZapsCreateZapRequest as ZapsCreateZapRequestPydantic
from zapier_embed_python_sdk.pydantic.zap import Zap as ZapPydantic

# Query params
ExpandSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'expand': typing.Union[ExpandSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_expand = api_client.QueryParameter(
    name="expand",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationVndApijson = ZapsCreateZapRequestSchema


request_body_zaps_create_zap_request = api_client.RequestBody(
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationVndApijson),
    },
)
SchemaFor201ResponseBodyApplicationVndApijson = ZapsCreateZapResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: ZapsCreateZapResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: ZapsCreateZapResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationVndApijson),
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

    def _create_zap_mapped_args(
        self,
        items: Zap,
        expand: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if items is not None:
            _body["items"] = items
        args.body = _body
        if expand is not None:
            _query_params["expand"] = expand
        args.query = _query_params
        return args

    async def _acreate_zap_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.api+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a Zap
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_expand,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/zaps',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_zaps_create_zap_request.serialize(body, content_type)
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


    def _create_zap_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/vnd.api+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a Zap
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_expand,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/zaps',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_zaps_create_zap_request.serialize(body, content_type)
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


class CreateZapRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_zap(
        self,
        items: Zap,
        expand: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_zap_mapped_args(
            items=items,
            expand=expand,
        )
        return await self._acreate_zap_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def create_zap(
        self,
        items: Zap,
        expand: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_zap_mapped_args(
            items=items,
            expand=expand,
        )
        return self._create_zap_oapg(
            body=args.body,
            query_params=args.query,
        )

class CreateZap(BaseApi):

    async def acreate_zap(
        self,
        items: Zap,
        expand: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ZapsCreateZapResponsePydantic:
        raw_response = await self.raw.acreate_zap(
            items=items,
            expand=expand,
            **kwargs,
        )
        if validate:
            return ZapsCreateZapResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ZapsCreateZapResponsePydantic, raw_response.body)
    
    
    def create_zap(
        self,
        items: Zap,
        expand: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ZapsCreateZapResponsePydantic:
        raw_response = self.raw.create_zap(
            items=items,
            expand=expand,
        )
        if validate:
            return ZapsCreateZapResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ZapsCreateZapResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        items: Zap,
        expand: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_zap_mapped_args(
            items=items,
            expand=expand,
        )
        return await self._acreate_zap_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        items: Zap,
        expand: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_zap_mapped_args(
            items=items,
            expand=expand,
        )
        return self._create_zap_oapg(
            body=args.body,
            query_params=args.query,
        )

