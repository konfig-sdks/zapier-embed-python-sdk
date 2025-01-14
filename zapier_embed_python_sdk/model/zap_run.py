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


class ZapRun(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            start_time = schemas.DateTimeSchema
            end_time = schemas.DateTimeSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "delayed": "DELAYED",
                        "scheduled": "SCHEDULED",
                        "pending": "PENDING",
                        "error": "ERROR",
                        "halted": "HALTED",
                        "throttled": "THROTTLED",
                        "held": "HELD",
                        "filtered": "FILTERED",
                        "skipped": "SKIPPED",
                        "success": "SUCCESS",
                    }
                
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
            zap_title = schemas.StrSchema
            
            
            class steps(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ZapRunStep']:
                        return ZapRunStep
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ZapRunStep'], typing.List['ZapRunStep']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'steps':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ZapRunStep':
                    return super().__getitem__(i)
            data_in = schemas.StrSchema
            data_out = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "start_time": start_time,
                "end_time": end_time,
                "status": status,
                "zap_title": zap_title,
                "steps": steps,
                "data_in": data_in,
                "data_out": data_out,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_time"]) -> MetaOapg.properties.end_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zap_title"]) -> MetaOapg.properties.zap_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steps"]) -> MetaOapg.properties.steps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_in"]) -> MetaOapg.properties.data_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_out"]) -> MetaOapg.properties.data_out: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "start_time", "end_time", "status", "zap_title", "steps", "data_in", "data_out", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_time"]) -> typing.Union[MetaOapg.properties.start_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_time"]) -> typing.Union[MetaOapg.properties.end_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zap_title"]) -> typing.Union[MetaOapg.properties.zap_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steps"]) -> typing.Union[MetaOapg.properties.steps, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_in"]) -> typing.Union[MetaOapg.properties.data_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_out"]) -> typing.Union[MetaOapg.properties.data_out, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "start_time", "end_time", "status", "zap_title", "steps", "data_in", "data_out", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        start_time: typing.Union[MetaOapg.properties.start_time, str, datetime, schemas.Unset] = schemas.unset,
        end_time: typing.Union[MetaOapg.properties.end_time, str, datetime, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        zap_title: typing.Union[MetaOapg.properties.zap_title, str, schemas.Unset] = schemas.unset,
        steps: typing.Union[MetaOapg.properties.steps, list, tuple, schemas.Unset] = schemas.unset,
        data_in: typing.Union[MetaOapg.properties.data_in, str, schemas.Unset] = schemas.unset,
        data_out: typing.Union[MetaOapg.properties.data_out, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ZapRun':
        return super().__new__(
            cls,
            *args,
            id=id,
            start_time=start_time,
            end_time=end_time,
            status=status,
            zap_title=zap_title,
            steps=steps,
            data_in=data_in,
            data_out=data_out,
            _configuration=_configuration,
            **kwargs,
        )

from zapier_embed_python_sdk.model.zap_run_step import ZapRunStep
