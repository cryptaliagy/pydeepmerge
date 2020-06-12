import pytest

from pydeepmerge import prefer_right
from pydeepmerge.types import Key


@pytest.mark.unit
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((Key.KeyNotFound, 1), 1),
        ((1, 2), 2),
        ((1, {1: 1}), {1: 1}),
        (({1: 1}, 1), 1),
        (({1: 1, 2: 2}, {1: 2}), {1: 2, 2: 2})
    ]
)
def test_prefer_right(test_input, expected):
    assert prefer_right(*test_input) == expected
