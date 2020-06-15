import operator

import pytest

from pydeepmerge import deep_merge
from pydeepmerge.strategies import meta_operator_merge


def return_right(left, right):
    return right


@pytest.mark.unit
@pytest.mark.parametrize(
    "op,mixed,raise_,test_input,expected",
    [
        (
            operator.add, False, False,
            (
                {"a": 1, "b": 1},
                {"a": 2, "c": 2},
            ),
            {"a": 3, "b": 1, "c": 2},
        ),
        (
            operator.add, False, False,
            (
                {"a": 1, "b": {"a": 1, "b": 1}, "c": {}},
                {"a": 2, "b": {"a": 2, "c": 2}, "d": 2},
            ),
            {"a": 3, "b": {"a": 3, "b": 1, "c": 2}, "c": {}, "d": 2},
        ),
        (
            return_right, False, True,
            (
                {"a": 1, "b": {}},
                {"a": 2, "b": 2},
            ),
            {"a": 3, "b": 1},
        ),
        (
            return_right, False, True,
            (
                {"a": 1, "b": 1},
                {"a": 2, "b": {}},
            ),
            {"a": 3, "b": 1},
        ),
        (
            operator.add, return_right, False,
            (
                {"a": 1, "b": {}},
                {"a": 2, "b": 2},
            ),
            {"a": 3, "b": 2},
        ),
        (
            operator.add, return_right, False,
            (
                {"a": 1, "b": 1},
                {"a": 2, "b": {}},
            ),
            {"a": 3, "b": {}},
        ),
        (
            return_right, True, False,
            (
                {"a": 1, "b": {}},
                {"a": 2, "b": 2},
            ),
            {"a": 2, "b": 2},
        ),
        (
            return_right, True, False,
            (
                {"a": 1, "b": 1},
                {"a": 2, "b": {}},
            ),
            {"a": 2, "b": {}},
        ),
    ]
)
def test_meta_operator_merge(op, mixed, raise_, test_input, expected):
    merge_strategy = meta_operator_merge(op, mixed)
    if raise_:
        with pytest.raises(TypeError):
            deep_merge(
                *test_input,
                merge_strategy=merge_strategy
            )
    else:
        assert deep_merge(
            *test_input,
            merge_strategy=merge_strategy
        ) == expected
