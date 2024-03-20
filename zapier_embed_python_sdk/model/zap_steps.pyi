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


class ZapSteps(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An ordered list of steps that define the logic of the Zap.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ZapStepsItem']:
            return ZapStepsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ZapStepsItem'], typing.List['ZapStepsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ZapSteps':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ZapStepsItem':
        return super().__getitem__(i)

from zapier_embed_python_sdk.model.zap_steps_item import ZapStepsItem
