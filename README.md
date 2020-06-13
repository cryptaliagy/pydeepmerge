# DeepMerge

[![build status](https://img.shields.io/github/workflow/status/taliamax/pydeepmerge/build)](https://github.com/taliamax/pydeepmerge/actions?query=workflow%3Abuild) [![release status](https://img.shields.io/github/workflow/status/taliamax/pydeepmerge/release?label=release)](https://github.com/taliamax/pydeepmerge/actions?query=workflow%3Arelease) [![MIT license](https://img.shields.io/pypi/l/pydeepmerge)](https://github.com/taliamax/pydeepmerge/blob/master/LICENSE) [![coverage status](https://img.shields.io/coveralls/github/taliamax/pydeepmerge)](https://coveralls.io/github/taliamax/pydeepmerge)

[![pypi version](https://img.shields.io/pypi/v/pydeepmerge)](https://pypi.org/project/pydeepmerge/) [![pypi python versions supported](https://img.shields.io/pypi/pyversions/pydeepmerge)](https://pypi.org/project/pydeepmerge/) [![pypi downloads](https://img.shields.io/pypi/dm/pydeepmerge)](https://pypi.org/project/pydeepmerge/)

A lightweight python package for performing deep-merges of python dictionaries

## Installation

Install this package with pip!

```bash
$ pip install pydeepmerge
```

To install this package from source, clone the repo and run:

```bash
$ pip install .
```

If you would like to develop, remember to install the extras.

```bash
# for bash
$ pip install -e .[test,dev]
# for zsh
$ pip install -e .\[test,dev\]
```

## Usage

Usage is simple:

```python
from pydeepmerge import deep_merge

> some_data = {'foo': {'bar': 'baz', 'spam': 'eggs'}, 'ham': 'eggs'}
> more_data = {'spam': {'eggs': 'ham'}, 'foo': {'baz': 'bar', 'bar': 'foo'}}
> deep_merge(some_data, more_data)
{'foo': {'bar': 'foo', 'baz': 'bar', 'spam': 'eggs'}, 'spam': {'eggs': 'ham'}, 'ham': 'eggs'}
```

`pydeepmerge` also allows users to specify their own merge strategy function. By default, it uses the function `prefer_right`.

A merge strategy is any function that can accept exactly two inputs. The output of the merge strategy function should be what the merge result between two values should be.

When writing your own merge strategy function, keep in mind that if the key does not exist on the left-hand mapping, the value `Key.NoKeyFound` will be passed to the first parameter of the function. This is done deliberately so the user can determine if they want to do special behaviour if it is the first occurrence of the key in the sequence of dictionaries.

An example of a merge strategy function can be found below:

```python
from pydeepmerge import deep_merge
from pydeepmerge.types import Key
from typing import Mapping

def pick_shallower(left_value, right_value):
    if left_value is Key.NoKeyFound:
        return right_value

    if isinstance(right_value, Mapping):
        if not isinstance(left_value, Mapping):
            return left_value
        return deep_merge(left_value, right_value)

    return right_value
```

The `deep_merge` function does not mutate any mapping but instead creates a new dictionary.
