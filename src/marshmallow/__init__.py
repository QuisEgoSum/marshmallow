from __future__ import annotations

from packaging.version import Version

from .decorators import (
    post_dump,
    post_load,
    pre_dump,
    pre_load,
    validates,
    validates_schema,
)
from .exceptions import ValidationError
from .schema import Schema, SchemaOpts
from .utils import EXCLUDE, INCLUDE, RAISE, missing, pprint

from . import dataclass_fields
from . import fields

__version__ = "3.17.0"
__parsed_version__ = Version(__version__)
__version_info__: tuple[int, int, int] | tuple[
    int, int, int, str, int
] = __parsed_version__.release  # type: ignore[assignment]
if __parsed_version__.pre:
    __version_info__ += __parsed_version__.pre  # type: ignore[assignment]
__all__ = [
    "EXCLUDE",
    "INCLUDE",
    "RAISE",
    "Schema",
    "SchemaOpts",
    "fields",
    "validates",
    "validates_schema",
    "pre_dump",
    "post_dump",
    "pre_load",
    "post_load",
    "pprint",
    "ValidationError",
    "missing",
]
