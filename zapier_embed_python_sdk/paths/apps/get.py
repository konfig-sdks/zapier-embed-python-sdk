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

from zapier_embed_python_sdk.model.apps_list_popular401_response import AppsListPopular401Response as AppsListPopular401ResponseSchema
from zapier_embed_python_sdk.model.apps_list_popular_response import AppsListPopularResponse as AppsListPopularResponseSchema
from zapier_embed_python_sdk.model.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse as ActionsListAvailableActionsdefaultResponseSchema

from zapier_embed_python_sdk.type.apps_list_popular_response import AppsListPopularResponse
from zapier_embed_python_sdk.type.apps_list_popular401_response import AppsListPopular401Response
from zapier_embed_python_sdk.type.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse

from ...api_client import Dictionary
from zapier_embed_python_sdk.pydantic.apps_list_popular401_response import AppsListPopular401Response as AppsListPopular401ResponsePydantic
from zapier_embed_python_sdk.pydantic.actions_list_available_actionsdefault_response import ActionsListAvailableActionsdefaultResponse as ActionsListAvailableActionsdefaultResponsePydantic
from zapier_embed_python_sdk.pydantic.apps_list_popular_response import AppsListPopularResponse as AppsListPopularResponsePydantic

from . import path

# Query params
LimitSchema = schemas.IntSchema
OffsetSchema = schemas.IntSchema
CategorySchema = schemas.StrSchema
QuerySchema = schemas.StrSchema
IdsSchema = schemas.StrSchema
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
        'category': typing.Union[CategorySchema, str, ],
        'query': typing.Union[QuerySchema, str, ],
        'ids': typing.Union[IdsSchema, str, ],
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
request_query_category = api_client.QueryParameter(
    name="category",
    style=api_client.ParameterStyle.FORM,
    schema=CategorySchema,
    explode=True,
)
request_query_query = api_client.QueryParameter(
    name="query",
    style=api_client.ParameterStyle.FORM,
    schema=QuerySchema,
    explode=True,
)
request_query_ids = api_client.QueryParameter(
    name="ids",
    style=api_client.ParameterStyle.FORM,
    schema=IdsSchema,
    explode=True,
)
_auth = [
    'OAuth2',
    'OAuth2',
]
SchemaFor200ResponseBodyApplicationVndApijson = AppsListPopularResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AppsListPopularResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AppsListPopularResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndApijson),
    },
)
SchemaFor401ResponseBodyApplicationVndApijson = AppsListPopular401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: AppsListPopular401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: AppsListPopular401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndApijson),
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
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/vnd.api+json',
)


class BaseApi(api_client.Api):

    def _list_popular_mapped_args(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if category is not None:
            _query_params["category"] = category
        if query is not None:
            _query_params["query"] = query
        if ids is not None:
            _query_params["ids"] = ids
        args.query = _query_params
        return args

    async def _alist_popular_oapg(
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
        Get Apps
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
            request_query_category,
            request_query_query,
            request_query_ids,
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
            path_template='/apps',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


    def _list_popular_oapg(
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
        Get Apps
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
            request_query_category,
            request_query_query,
            request_query_ids,
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
            path_template='/apps',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


class ListPopularRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_popular(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_popular_mapped_args(
            limit=limit,
            offset=offset,
            category=category,
            query=query,
            ids=ids,
        )
        return await self._alist_popular_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_popular(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_popular_mapped_args(
            limit=limit,
            offset=offset,
            category=category,
            query=query,
            ids=ids,
        )
        return self._list_popular_oapg(
            query_params=args.query,
        )

class ListPopular(BaseApi):

    async def alist_popular(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AppsListPopularResponsePydantic:
        raw_response = await self.raw.alist_popular(
            limit=limit,
            offset=offset,
            category=category,
            query=query,
            ids=ids,
            **kwargs,
        )
        if validate:
            return AppsListPopularResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AppsListPopularResponsePydantic, raw_response.body)
    
    
    def list_popular(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AppsListPopularResponsePydantic:
        raw_response = self.raw.list_popular(
            limit=limit,
            offset=offset,
            category=category,
            query=query,
            ids=ids,
        )
        if validate:
            return AppsListPopularResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AppsListPopularResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_popular_mapped_args(
            limit=limit,
            offset=offset,
            category=category,
            query=query,
            ids=ids,
        )
        return await self._alist_popular_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        category: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_popular_mapped_args(
            limit=limit,
            offset=offset,
            category=category,
            query=query,
            ids=ids,
        )
        return self._list_popular_oapg(
            query_params=args.query,
        )

