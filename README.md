# DeepMerge

A simple python package for performing deep-merges of python dictionaries

Usage is simple:

```python
from deepmerge import deep_merge

> some_data = {'foo': {'bar': 'baz'}}
> more_data = {'spam': {'eggs': 'ham'}, 'foo': {'baz': 'bar', 'bar': 'foo'}}
> deep_merge(some_data, more_data)
{'foo': {'bar': 'foo', 'baz': 'bar'}, 'spam': {'eggs': 'ham'}}
```