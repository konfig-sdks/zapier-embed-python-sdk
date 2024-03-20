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


class AuthenticationsCreateNewAuthenticationRequestData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "app",
            "authentication_fields",
            "title",
        }
        
        class properties:
            
            
            class title(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            app = schemas.UUIDSchema
            authentication_fields = schemas.DictSchema
            __annotations__ = {
                "title": title,
                "app": app,
                "authentication_fields": authentication_fields,
            }
    
    app: MetaOapg.properties.app
    authentication_fields: MetaOapg.properties.authentication_fields
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app"]) -> MetaOapg.properties.app: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication_fields"]) -> MetaOapg.properties.authentication_fields: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "app", "authentication_fields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app"]) -> MetaOapg.properties.app: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentication_fields"]) -> MetaOapg.properties.authentication_fields: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "app", "authentication_fields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        app: typing.Union[MetaOapg.properties.app, str, uuid.UUID, ],
        authentication_fields: typing.Union[MetaOapg.properties.authentication_fields, dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthenticationsCreateNewAuthenticationRequestData':
        return super().__new__(
            cls,
            *args,
            app=app,
            authentication_fields=authentication_fields,
            title=title,
            _configuration=_configuration,
            **kwargs,
        )
