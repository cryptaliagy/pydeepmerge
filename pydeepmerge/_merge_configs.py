from pathlib import Path

from pydeepmerge import deep_merge
from pydeepmerge.errors import (
    FileTypeError,
    ParserNotAvailableError
)
from pydeepmerge.parsers import load_parsers
from pydeepmerge.strategies import prefer_right
from pydeepmerge.types import MergeStrategy
from typing import (
    Dict,
    List,
)


def merge_configs(
    *files: List[str],
    merge_strategy: MergeStrategy = prefer_right,
    auto: bool = True,
    strict: bool = True,
    extra_parsers: Dict = {}
) -> Dict:
    '''
    A function that takes a sequence of config filenames and produces
    a dictionary resulting from all the files being processed and then merged
    with a specified merge strategy.

    To use custom parsers, pass a flat dictionary of filetypes and parsers.
    If `auto` is set to False, use only the parsers explicitly passed
    through the `extra_parsers` parameter.

    If `strict` is set to True, all file names must have the same extension.
    This also applies to file type variations like `.yml` vs `.yaml`
    '''

    if strict:
        file_iter = iter(files)
        first_file_name = next(file_iter)

        file_type = Path(first_file_name).suffix

        if file_type == '':
            raise FileTypeError(
                'File "%s" has no file type extension' % first_file_name
            )

        for file_name in file_iter:
            if Path(file_name).suffix != file_type:
                raise FileTypeError(
                    'File "%s" has improper filetype. '
                    'Expected file type of "%s"' % (file_name, file_type)
                )

    parsers = {}
    if auto:
        parsers = load_parsers()

    parsers.update(extra_parsers)

    file_data = []

    for file_name in files:
        file_type = Path(file_name).suffix

        if file_type not in parsers:
            raise ParserNotAvailableError('No parser for "%s"' % file_type)

        parser = parsers[file_type]
        file_data.append(parser(file_name))

    return deep_merge(*file_data, merge_strategy=merge_strategy)
