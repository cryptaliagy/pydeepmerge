import pytest
from unittest.mock import patch
from pydeepmerge import merge_configs
from pydeepmerge.errors import (
    FileTypeError,
    ParserNotAvailableError
)


@pytest.mark.unit
@pytest.mark.parametrize(
    'parser_returns,expected_result',
    [
        (
            [{'foo': 'spam', 'egg': 'ham'}, {'bar': 'baz', 'spam': 'eggs'}],
            {'foo': 'spam', 'egg': 'ham', 'bar': 'baz', 'spam': 'eggs'}
        ),
        (
            [{'foo': 'spam', 'egg': 'ham'}, {'bar': 'baz', 'foo': 'ham'}],
            {'foo': 'ham', 'egg': 'ham', 'bar': 'baz'}
        ),
    ]
)
@patch('pydeepmerge.parsers.json.json_parser')
def test_merge_configs(mock_json_parser, parser_returns, expected_result):
    mock_json_parser.side_effect = parser_returns

    assert merge_configs('foo.json', 'bar.json') == expected_result


@pytest.mark.unit
@pytest.mark.parametrize(
    'exception_class,test_files',
    [
        (FileTypeError, ['foo', 'bar.json']),
        (FileTypeError, ['foo.json', 'bar.yaml']),
        (ParserNotAvailableError, ['foo.yaml', 'bar.yaml'])
    ]
)
@patch('pydeepmerge._merge_configs.load_parsers')
def test_merge_config_fail(mock_load_parser, exception_class, test_files):
    mock_load_parser.return_value = {'.json': lambda x: x}
    with pytest.raises(exception_class):
        merge_configs(*test_files)
