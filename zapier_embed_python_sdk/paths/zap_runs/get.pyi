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

from zapier_embed_python_sdk.model.experimental_get_zap_runs403_response import ExperimentalGetZapRuns403Response as ExperimentalGetZapRuns403ResponseSchema
from zapier_embed_python_sdk.model.experimental_get_zap_runs_response import ExperimentalGetZapRunsResponse as ExperimentalGetZapRunsResponseSchema
from zapier_embed_python_sdk.model.experimental_get_zap_runs401_response import ExperimentalGetZapRuns401Response as ExperimentalGetZapRuns401ResponseSchema

from zapier_embed_python_sdk.type.experimental_get_zap_runs_response import ExperimentalGetZapRunsResponse
from zapier_embed_python_sdk.type.experimental_get_zap_runs401_response import ExperimentalGetZapRuns401Response
from zapier_embed_python_sdk.type.experimental_get_zap_runs403_response import ExperimentalGetZapRuns403Response

from ...api_client import Dictionary
from zapier_embed_python_sdk.pydantic.experimental_get_zap_runs403_response import ExperimentalGetZapRuns403Response as ExperimentalGetZapRuns403ResponsePydantic
from zapier_embed_python_sdk.pydantic.experimental_get_zap_runs_response import ExperimentalGetZapRunsResponse as ExperimentalGetZapRunsResponsePydantic
from zapier_embed_python_sdk.pydantic.experimental_get_zap_runs401_response import ExperimentalGetZapRuns401Response as ExperimentalGetZapRuns401ResponsePydantic

# Query params
FromDateSchema = schemas.StrSchema
ToDateSchema = schemas.StrSchema
ZapIdSchema = schemas.StrSchema
LimitSchema = schemas.IntSchema
OffsetSchema = schemas.IntSchema


class SearchSchema(
    schemas.StrSchema
):
    pass


class StatusesSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DELAYED(cls):
        return cls("delayed")
    
    @schemas.classproperty
    def SCHEDULED(cls):
        return cls("scheduled")
    
    @schemas.classproperty
    def PENDING(cls):
        return cls("pending")
    
    @schemas.classproperty
    def ERROR(cls):
        return cls("error")
    
    @schemas.classproperty
    def ERROR_HANDLED(cls):
        return cls("error_handled")
    
    @schemas.classproperty
    def HALTED(cls):
        return cls("halted")
    
    @schemas.classproperty
    def THROTTLED(cls):
        return cls("throttled")
    
    @schemas.classproperty
    def HELD(cls):
        return cls("held")
    
    @schemas.classproperty
    def FILTERED(cls):
        return cls("filtered")
    
    @schemas.classproperty
    def SKIPPED(cls):
        return cls("skipped")
    
    @schemas.classproperty
    def SUCCESS(cls):
        return cls("success")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'from_date': typing.Union[FromDateSchema, str, ],
        'to_date': typing.Union[ToDateSchema, str, ],
        'zap_id': typing.Union[ZapIdSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
        'search': typing.Union[SearchSchema, str, ],
        'statuses': typing.Union[StatusesSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_from_date = api_client.QueryParameter(
    name="from_date",
    style=api_client.ParameterStyle.FORM,
    schema=FromDateSchema,
    explode=True,
)
request_query_to_date = api_client.QueryParameter(
    name="to_date",
    style=api_client.ParameterStyle.FORM,
    schema=ToDateSchema,
    explode=True,
)
request_query_zap_id = api_client.QueryParameter(
    name="zap_id",
    style=api_client.ParameterStyle.FORM,
    schema=ZapIdSchema,
    explode=True,
)
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
request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
request_query_statuses = api_client.QueryParameter(
    name="statuses",
    style=api_client.ParameterStyle.FORM,
    schema=StatusesSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ExperimentalGetZapRunsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ExperimentalGetZapRunsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ExperimentalGetZapRunsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ExperimentalGetZapRuns401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ExperimentalGetZapRuns401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ExperimentalGetZapRuns401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ExperimentalGetZapRuns403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ExperimentalGetZapRuns403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ExperimentalGetZapRuns403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_zap_runs_mapped_args(
        self,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        zap_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        statuses: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if from_date is not None:
            _query_params["from_date"] = from_date
        if to_date is not None:
            _query_params["to_date"] = to_date
        if zap_id is not None:
            _query_params["zap_id"] = zap_id
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if search is not None:
            _query_params["search"] = search
        if statuses is not None:
            _query_params["statuses"] = statuses
        args.query = _query_params
        return args

    async def _aget_zap_runs_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Zap Runs
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_from_date,
            request_query_to_date,
            request_query_zap_id,
            request_query_limit,
            request_query_offset,
            request_query_search,
            request_query_statuses,
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
            path_template='/zap-runs',
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
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


    def _get_zap_runs_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Zap Runs
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_from_date,
            request_query_to_date,
            request_query_zap_id,
            request_query_limit,
            request_query_offset,
            request_query_search,
            request_query_statuses,
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
            path_template='/zap-runs',
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetZapRunsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_zap_runs(
        self,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        zap_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        statuses: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_zap_runs_mapped_args(
            from_date=from_date,
            to_date=to_date,
            zap_id=zap_id,
            limit=limit,
            offset=offset,
            search=search,
            statuses=statuses,
        )
        return await self._aget_zap_runs_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_zap_runs(
        self,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        zap_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        statuses: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_zap_runs_mapped_args(
            from_date=from_date,
            to_date=to_date,
            zap_id=zap_id,
            limit=limit,
            offset=offset,
            search=search,
            statuses=statuses,
        )
        return self._get_zap_runs_oapg(
            query_params=args.query,
        )

class GetZapRuns(BaseApi):

    async def aget_zap_runs(
        self,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        zap_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        statuses: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ExperimentalGetZapRunsResponsePydantic:
        raw_response = await self.raw.aget_zap_runs(
            from_date=from_date,
            to_date=to_date,
            zap_id=zap_id,
            limit=limit,
            offset=offset,
            search=search,
            statuses=statuses,
            **kwargs,
        )
        if validate:
            return ExperimentalGetZapRunsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ExperimentalGetZapRunsResponsePydantic, raw_response.body)
    
    
    def get_zap_runs(
        self,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        zap_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        statuses: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ExperimentalGetZapRunsResponsePydantic:
        raw_response = self.raw.get_zap_runs(
            from_date=from_date,
            to_date=to_date,
            zap_id=zap_id,
            limit=limit,
            offset=offset,
            search=search,
            statuses=statuses,
        )
        if validate:
            return ExperimentalGetZapRunsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ExperimentalGetZapRunsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        zap_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        statuses: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_zap_runs_mapped_args(
            from_date=from_date,
            to_date=to_date,
            zap_id=zap_id,
            limit=limit,
            offset=offset,
            search=search,
            statuses=statuses,
        )
        return await self._aget_zap_runs_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        from_date: typing.Optional[str] = None,
        to_date: typing.Optional[str] = None,
        zap_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        statuses: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_zap_runs_mapped_args(
            from_date=from_date,
            to_date=to_date,
            zap_id=zap_id,
            limit=limit,
            offset=offset,
            search=search,
            statuses=statuses,
        )
        return self._get_zap_runs_oapg(
            query_params=args.query,
        )

