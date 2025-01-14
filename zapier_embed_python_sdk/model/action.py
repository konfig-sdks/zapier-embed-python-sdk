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


class Action(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An Action is an operation that can be performed against a third-party API; either a read or a write. A Zap is composed of a read, followed by one or more writes.
    """


    class MetaOapg:
        required = {
            "app",
            "action_type",
            "is_instant",
            "description",
            "id",
            "title",
            "type",
            "key",
        }
        
        class properties:
            title = schemas.StrSchema
            description = schemas.StrSchema
            type = schemas.StrSchema
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[\w-]+:[\w-]+$',
                    }]
            key = schemas.StrSchema
            
            
            class action_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "READ": "READ",
                        "WRITE": "WRITE",
                    }
                
                @schemas.classproperty
                def READ(cls):
                    return cls("READ")
                
                @schemas.classproperty
                def WRITE(cls):
                    return cls("WRITE")
            
            
            class app(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class one_of_0(
                        schemas.UUIDBase,
                        schemas.AnyTypeSchema,
                    ):
                    
                    
                        class MetaOapg:
                            format = 'uuid'
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'one_of_0':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            App,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'app':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            is_instant = schemas.BoolSchema
            __annotations__ = {
                "title": title,
                "description": description,
                "type": type,
                "id": id,
                "key": key,
                "action_type": action_type,
                "app": app,
                "is_instant": is_instant,
            }
    
    app: MetaOapg.properties.app
    action_type: MetaOapg.properties.action_type
    is_instant: MetaOapg.properties.is_instant
    description: MetaOapg.properties.description
    id: MetaOapg.properties.id
    title: MetaOapg.properties.title
    type: MetaOapg.properties.type
    key: MetaOapg.properties.key
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action_type"]) -> MetaOapg.properties.action_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app"]) -> MetaOapg.properties.app: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_instant"]) -> MetaOapg.properties.is_instant: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "type", "id", "key", "action_type", "app", "is_instant", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action_type"]) -> MetaOapg.properties.action_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app"]) -> MetaOapg.properties.app: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_instant"]) -> MetaOapg.properties.is_instant: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "type", "id", "key", "action_type", "app", "is_instant", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        app: typing.Union[MetaOapg.properties.app, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        action_type: typing.Union[MetaOapg.properties.action_type, str, ],
        is_instant: typing.Union[MetaOapg.properties.is_instant, bool, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Action':
        return super().__new__(
            cls,
            *args,
            app=app,
            action_type=action_type,
            is_instant=is_instant,
            description=description,
            id=id,
            title=title,
            type=type,
            key=key,
            _configuration=_configuration,
            **kwargs,
        )

from zapier_embed_python_sdk.model.app import App
