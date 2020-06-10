from collections.abc import Mapping
from typing import List, Dict

def deep_merge(*mappings: List[Mapping]) -> Dict:
    '''
    Accepts a series of mappings and produces a dictionary of
    all the mappings deep-merged so only leaves are replaced
    '''
    result = {}
    for mapping in mappings:
        for key, value in mapping.items():
            if isinstance(value, Mapping):
                existing = result.get(key, {})
                if not isinstance(existing, Mapping):
                    existing = {}
                result[key] = deep_merge(existing, value)
            else:
                result[key] = value
    return result
