import pytest
from unittest.mock import patch
from pydeepmerge import merge_configs
from pydeepmerge.errors import (
    FileTypeError,
    ParserNotAvailableError
)


@pytest.mark.unit
@patch('pydeepmerge.parsers.json.json_parser')
def test_merge_configs(mock_json_parser):
    mock_json_parser.side_effect = [
        {'foo': 'spam', 'egg': 'ham'},
        {'foo': 'bar', 'baz': 'egg'}
    ]

    expected_return = {
        'foo': 'bar',
        'egg': 'ham',
        'baz': 'egg'
    }

    assert merge_configs('foo.json', 'bar.json') == expected_return


@pytest.mark.unit
@pytest.mark.parametrize(
    'exception_class,test_files',
    [
        (FileTypeError, ['foo', 'bar.json']),
        (FileTypeError, ['foo.json', 'bar.yaml']),
        (ParserNotAvailableError, ['foo.yaml', 'bar.yaml'])
    ]
)
@patch('pydeepmerge.parsers.load_parsers')
def test_merge_config_fail(mock_load_parser, exception_class, test_files):
    mock_load_parser.return_value = {'.json': lambda x: x}
    with pytest.raises(exception_class):
        merge_configs(*test_files)
