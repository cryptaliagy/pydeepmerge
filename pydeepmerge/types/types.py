import enum
from typing import (
    Any,
    Callable
)


class Key(enum.Enum):
    KeyNotFound = 1


MergeStrategy = Callable[[Any, Any], Any]
