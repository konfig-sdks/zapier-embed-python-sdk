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

from zapier_embed_python_sdk.model.zaps_get_filtered_zaps403_response import ZapsGetFilteredZaps403Response as ZapsGetFilteredZaps403ResponseSchema
from zapier_embed_python_sdk.model.zaps_get_filtered_zaps401_response import ZapsGetFilteredZaps401Response as ZapsGetFilteredZaps401ResponseSchema
from zapier_embed_python_sdk.model.zaps_get_filtered_zaps_response import ZapsGetFilteredZapsResponse as ZapsGetFilteredZapsResponseSchema
from zapier_embed_python_sdk.model.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse as ActionsListAvailableActionsdefaultResponseSchema

from zapier_embed_python_sdk.type.zaps_get_filtered_zaps401_response import ZapsGetFilteredZaps401Response
from zapier_embed_python_sdk.type.zaps_get_filtered_zaps_response import ZapsGetFilteredZapsResponse
from zapier_embed_python_sdk.type.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse
from zapier_embed_python_sdk.type.zaps_get_filtered_zaps403_response import ZapsGetFilteredZaps403Response

from ...api_client import Dictionary
from zapier_embed_python_sdk.pydantic.zaps_get_filtered_zaps_response import ZapsGetFilteredZapsResponse as ZapsGetFilteredZapsResponsePydantic
from zapier_embed_python_sdk.pydantic.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse as ActionsListAvailableActionsdefaultResponsePydantic
from zapier_embed_python_sdk.pydantic.zaps_get_filtered_zaps403_response import ZapsGetFilteredZaps403Response as ZapsGetFilteredZaps403ResponsePydantic
from zapier_embed_python_sdk.pydantic.zaps_get_filtered_zaps401_response import ZapsGetFilteredZaps401Response as ZapsGetFilteredZaps401ResponsePydantic

# Query params
LimitSchema = schemas.IntSchema
OffsetSchema = schemas.IntSchema


class InputsSchema(
    schemas.DictSchema
):


    class MetaOapg:
        additional_properties = schemas.StrSchema
    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
    ) -> 'InputsSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
ExpandSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
        'inputs': typing.Union[InputsSchema, dict, frozendict.frozendict, ],
        'expand': typing.Union[ExpandSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_inputs = api_client.QueryParameter(
    name="inputs",
    style=api_client.ParameterStyle.DEEP_OBJECT,
    schema=InputsSchema,
)
request_query_expand = api_client.QueryParameter(
    name="expand",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationVndApijson = ZapsGetFilteredZapsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ZapsGetFilteredZapsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ZapsGetFilteredZapsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndApijson),
    },
)
SchemaFor401ResponseBodyApplicationVndApijson = ZapsGetFilteredZaps401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ZapsGetFilteredZaps401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ZapsGetFilteredZaps401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndApijson),
    },
)
SchemaFor403ResponseBodyApplicationVndApijson = ZapsGetFilteredZaps403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ZapsGetFilteredZaps403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ZapsGetFilteredZaps403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndApijson),
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

    def _get_filtered_zaps_mapped_args(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        inputs: typing.Optional[typing.Dict[str, str]] = None,
        expand: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if inputs is not None:
            _query_params["inputs"] = inputs
        if expand is not None:
            _query_params["expand"] = expand
        args.query = _query_params
        return args

    async def _aget_filtered_zaps_oapg(
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
        Get Zaps
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_offset,
            request_query_inputs,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/zaps',
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


    def _get_filtered_zaps_oapg(
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
        Get Zaps
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_offset,
            request_query_inputs,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/zaps',
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


class GetFilteredZapsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_filtered_zaps(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        inputs: typing.Optional[typing.Dict[str, str]] = None,
        expand: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_filtered_zaps_mapped_args(
            limit=limit,
            offset=offset,
            inputs=inputs,
            expand=expand,
        )
        return await self._aget_filtered_zaps_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_filtered_zaps(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        inputs: typing.Optional[typing.Dict[str, str]] = None,
        expand: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_filtered_zaps_mapped_args(
            limit=limit,
            offset=offset,
            inputs=inputs,
            expand=expand,
        )
        return self._get_filtered_zaps_oapg(
            query_params=args.query,
        )

class GetFilteredZaps(BaseApi):

    async def aget_filtered_zaps(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        inputs: typing.Optional[typing.Dict[str, str]] = None,
        expand: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ZapsGetFilteredZapsResponsePydantic:
        raw_response = await self.raw.aget_filtered_zaps(
            limit=limit,
            offset=offset,
            inputs=inputs,
            expand=expand,
            **kwargs,
        )
        if validate:
            return ZapsGetFilteredZapsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ZapsGetFilteredZapsResponsePydantic, raw_response.body)
    
    
    def get_filtered_zaps(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        inputs: typing.Optional[typing.Dict[str, str]] = None,
        expand: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ZapsGetFilteredZapsResponsePydantic:
        raw_response = self.raw.get_filtered_zaps(
            limit=limit,
            offset=offset,
            inputs=inputs,
            expand=expand,
        )
        if validate:
            return ZapsGetFilteredZapsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ZapsGetFilteredZapsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        inputs: typing.Optional[typing.Dict[str, str]] = None,
        expand: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_filtered_zaps_mapped_args(
            limit=limit,
            offset=offset,
            inputs=inputs,
            expand=expand,
        )
        return await self._aget_filtered_zaps_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        inputs: typing.Optional[typing.Dict[str, str]] = None,
        expand: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_filtered_zaps_mapped_args(
            limit=limit,
            offset=offset,
            inputs=inputs,
            expand=expand,
        )
        return self._get_filtered_zaps_oapg(
            query_params=args.query,
        )

