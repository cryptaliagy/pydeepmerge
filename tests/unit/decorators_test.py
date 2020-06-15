import pytest

from pydeepmerge import deep_merge
from pydeepmerge.strategies.decorators import (
    recurse,
)


def return_right(left, right):
    return right


@pytest.mark.unit
@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            (
                {"a": 0, "b": {"a": 0, "b": {"a": 0, "b": 0}}},
                {"b": {"b": {"b": 1}}},
            ),
            {'a': 0, 'b': {'a': 0, 'b': {'a': 0, 'b': 1}}}
        ),
    ]
)
def test_recurse(test_input, expected):
    assert deep_merge(
        *test_input,
        merge_strategy=recurse(return_right)
    ) == expected
