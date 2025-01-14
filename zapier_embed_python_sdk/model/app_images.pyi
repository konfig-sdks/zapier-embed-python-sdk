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


class AppImages(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Images/icons of various resolutions to represent the app.
    """


    class MetaOapg:
        
        class properties:
            url_16x16 = schemas.StrSchema
            url_32x32 = schemas.StrSchema
            url_64x64 = schemas.StrSchema
            url_128x128 = schemas.StrSchema
            __annotations__ = {
                "url_16x16": url_16x16,
                "url_32x32": url_32x32,
                "url_64x64": url_64x64,
                "url_128x128": url_128x128,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url_16x16"]) -> MetaOapg.properties.url_16x16: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url_32x32"]) -> MetaOapg.properties.url_32x32: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url_64x64"]) -> MetaOapg.properties.url_64x64: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url_128x128"]) -> MetaOapg.properties.url_128x128: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["url_16x16", "url_32x32", "url_64x64", "url_128x128", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url_16x16"]) -> typing.Union[MetaOapg.properties.url_16x16, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url_32x32"]) -> typing.Union[MetaOapg.properties.url_32x32, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url_64x64"]) -> typing.Union[MetaOapg.properties.url_64x64, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url_128x128"]) -> typing.Union[MetaOapg.properties.url_128x128, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["url_16x16", "url_32x32", "url_64x64", "url_128x128", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        url_16x16: typing.Union[MetaOapg.properties.url_16x16, str, schemas.Unset] = schemas.unset,
        url_32x32: typing.Union[MetaOapg.properties.url_32x32, str, schemas.Unset] = schemas.unset,
        url_64x64: typing.Union[MetaOapg.properties.url_64x64, str, schemas.Unset] = schemas.unset,
        url_128x128: typing.Union[MetaOapg.properties.url_128x128, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppImages':
        return super().__new__(
            cls,
            *args,
            url_16x16=url_16x16,
            url_32x32=url_32x32,
            url_64x64=url_64x64,
            url_128x128=url_128x128,
            _configuration=_configuration,
            **kwargs,
        )
