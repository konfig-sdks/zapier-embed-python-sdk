# coding: utf-8

"""
    Zapier Embed API

    The Zapier Embed API.

    The version of the OpenAPI document: 1.0.0
    Contact: contact@zapier.com
    Created by: https://help.zapier.com/hc/en-us
"""

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


class InputsWithAuthenticationId(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The common data object that includes inputs and an authentication id.
    """


    class MetaOapg:
        required = {
            "inputs",
            "authentication",
        }
        
        class properties:
            authentication = schemas.AnyTypeSchema
            inputs = schemas.DictSchema
            limit = schemas.Int32Schema
            offset = schemas.Int32Schema
            __annotations__ = {
                "authentication": authentication,
                "inputs": inputs,
                "limit": limit,
                "offset": offset,
            }
    
    inputs: MetaOapg.properties.inputs
    authentication: MetaOapg.properties.authentication
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication"]) -> MetaOapg.properties.authentication: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputs"]) -> MetaOapg.properties.inputs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["authentication", "inputs", "limit", "offset", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentication"]) -> MetaOapg.properties.authentication: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputs"]) -> MetaOapg.properties.inputs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> typing.Union[MetaOapg.properties.limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["offset"]) -> typing.Union[MetaOapg.properties.offset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authentication", "inputs", "limit", "offset", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        inputs: typing.Union[MetaOapg.properties.inputs, dict, frozendict.frozendict, ],
        authentication: typing.Union[MetaOapg.properties.authentication, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        limit: typing.Union[MetaOapg.properties.limit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        offset: typing.Union[MetaOapg.properties.offset, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InputsWithAuthenticationId':
        return super().__new__(
            cls,
            *args,
            inputs=inputs,
            authentication=authentication,
            limit=limit,
            offset=offset,
            _configuration=_configuration,
            **kwargs,
        )
