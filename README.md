# DeepMerge

A simple python package for performing deep-merges of python dictionaries

Usage is simple:

```python
from pydeepmerge import deep_merge

> some_data = {'foo': {'bar': 'baz', 'spam': 'eggs'}, 'ham': 'eggs'}
> more_data = {'spam': {'eggs': 'ham'}, 'foo': {'baz': 'bar', 'bar': 'foo'}}
> deep_merge(some_data, more_data)
{'foo': {'bar': 'foo', 'baz': 'bar', 'spam': 'eggs'}, 'spam': {'eggs': 'ham'}, 'ham': 'eggs'}
```