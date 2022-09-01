from __future__ import annotations

import enum
import dataclasses

from . import fields
from .schema import Schema


def _field_wrapper(mh_field):
    return dataclasses.field(metadata=dict(schema=mh_field))


def datacls_to_schema(cls) -> Schema:
    schema_fields = dict()
    for field in dataclasses.fields(cls):
        schema_fields[field.name] = field.metadata['schema']
    return Schema(fields=schema_fields)


class String:
    def __new__(cls, **kwargs):
        return _field_wrapper(fields.String(**kwargs))


class Integer:
    def __new__(cls, **kwargs):
        return _field_wrapper(fields.Integer(**kwargs))


class Number:
    def __new__(cls, **kwargs):
        return _field_wrapper(fields.Number(**kwargs))


class Boolean:
    def __new__(cls, **kwargs):
        return _field_wrapper(fields.Boolean(**kwargs))


class List:
    def __new__(cls, instance, **kwargs):
        return _field_wrapper(fields.List(fields.Nested(datacls_to_schema(instance)), **kwargs))


class Email:
    def __new__(cls, **kwargs):
        return _field_wrapper(fields.Email(**kwargs))


class Enum:
    def __new__(cls, enum: enum.Enum | List, **kwargs):
        return _field_wrapper(fields.Enum(enum, **kwargs))


class Nested:
    def __new__(cls, instance, **kwargs):
        return _field_wrapper(fields.Nested(datacls_to_schema(instance), **kwargs))

