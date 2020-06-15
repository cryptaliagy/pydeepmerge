import pytest

from pydeepmerge import deep_merge
from pydeepmerge.strategies.decorators import (
    recurse,
    keep_default,
    disallow_mixed,
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


@pytest.mark.unit
@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            (
                {"a": 0, "b": 0},
                {"a": 1, "c": 1},
            ),
            {"a": 1, "b": 0, "c": 1}
        ),
    ]
)
def test_keep_default(test_input, expected):
    assert deep_merge(
        *test_input,
        merge_strategy=keep_default(return_right)
    ) == expected


@pytest.mark.unit
@pytest.mark.parametrize(
    "raise_,test_input,expected",
    [
        (
            False,
            (
                {"a": 0},
                {"a": 1},
            ),
            {"a": 1}
        ),
        (
            False,
            (
                {"a": {"a": 0}},
                {"a": {"b": 1}},
            ),
            {"a": {"b": 1}}
        ),
        (
            True,
            (
                {"a": {"a": 0}},
                {"a": 1},
            ),
            {"a": 1}
        ),
        (
            True,
            (
                {"a": 0},
                {"a": {"a": 1}},
            ),
            {"a": 1}
        ),
    ]
)
def test_disallow_mixed(raise_, test_input, expected):
    if raise_:
        with pytest.raises(TypeError):
            deep_merge(
                *test_input,
                merge_strategy=disallow_mixed(return_right)
            )
    else:
        assert deep_merge(
            *test_input,
            merge_strategy=disallow_mixed(return_right)
        ) == expected
