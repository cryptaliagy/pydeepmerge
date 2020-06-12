from collections.abc import Mapping
from pydeepmerge.types import Key
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
import logging

MergeStrategy = Callable[[Any, Any], Any]

logging.basicConfig(level=logging.INFO)


def prefer_right(left_value: Any, right_value: Any) -> Any:
    '''
    A merge strategy for prefering the right-hand value when
    merging Mappings while also recursing if the right-hand value
    is itself a Mapping
    '''
    logging.debug(
        "prefer_right: left_value: %s, right_value: %s",
        left_value,
        right_value
    )
    if left_value is Key.KeyNotFound:
        return right_value

    if isinstance(right_value, Mapping):
        if not isinstance(left_value, Mapping):
            left_value = {}
        return deep_merge(left_value, right_value, merge_strategy=prefer_right)

    return right_value


def deep_merge(
    *mappings: List[Mapping],
    merge_strategy: MergeStrategy = prefer_right
) -> Dict:
    '''
    Accepts a series of mappings and optionally a merge strategy
    and produces a dictionary from applying the merge strategy to the values

    The merge_strategy should be a function that accepts two values and returns
    whatever the value of the merge between those two values are. If the current
    dictionary does not have a key for the value in the merging dictionary,
    the input value of the left_value function will be Key.KeyNotFound.

    This type was used instead of None to allow for None to still be a
    valid value in a dictionary.
    '''
    result = {}
    for mapping in mappings:
        for key, right_value in mapping.items():
            logging.debug("deep_merge: key: %s", key)
            left_value = result.get(key, Key.KeyNotFound)
            result[key] = merge_strategy(left_value, right_value)
            logging.debug("result_dict: %s", result)
    return result
