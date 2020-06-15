import functools as ft
from typing import Mapping

from pydeepmerge import deep_merge
from pydeepmerge._deep_merge import MergeStrategy


def recurse(strategy: MergeStrategy) -> MergeStrategy:
    @ft.wraps(strategy)
    def newstrategy(left, right):
        if isinstance(left, Mapping) and isinstance(right, Mapping):
            return deep_merge(left, right, merge_strategy=newstrategy)
        return strategy(left, right)
    return newstrategy
