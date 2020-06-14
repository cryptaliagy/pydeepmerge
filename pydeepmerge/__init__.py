'''
A lightweight package to perform deep merges of Mapping objects
'''

import pydeepmerge.strategies as strategies
import pydeepmerge._deep_merge as _deep_merge

from pydeepmerge._deep_merge import deep_merge  # noqa: F401

# Since prefer_right is a merge strategy, it should be
# in the strategies subpackage, but it's also the default
# merge strategy, and recursive, so if it is not
# in the _deep_merge module it'll cause a circular
# import
strategies.prefer_right = _deep_merge.prefer_right

from pydeepmerge._merge_configs import merge_configs  # noqa: F401, E402
