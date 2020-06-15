from typing import Callable, Mapping, Union

from pydeepmerge._deep_merge import MergeStrategy
from pydeepmerge.strategies.decorators import (
    recurse,
    keep_default,
    disallow_mixed,
)


def meta_operator_merge(
    op: MergeStrategy,
    mixed: Union[bool, MergeStrategy] = False
) -> MergeStrategy:
    """
    Converts a binary operator `op` such as those from the
    `operator` package to a `MergeStrategy`.

    If `mixed` is `False`, and exactly one of `left` or
    `right` are `Mapping`s during a merge, then a
    `TypeError` is raised (this is the default).

    Therefore, if `mixed` is set to `True`, then the
    provided operator `op` must handle the case where
    exactly one of `left` or `right` is a mapping.

    Otherwise, `mixed` must be a `MergeStrategy` (a
    `Callable`) which handles this case.
    """
    @recurse
    @keep_default
    def operator_merge(left, right):
        if (isinstance(mixed, Callable)
            and (isinstance(left, Mapping) ^ isinstance(right, Mapping))
        ):  # noqa: E124
            return mixed(left, right)
        return op(left, right)
    if mixed:
        return operator_merge
    return disallow_mixed(operator_merge)
