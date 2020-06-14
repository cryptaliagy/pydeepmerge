import json


def json_parser(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
