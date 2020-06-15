from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def yaml_loader(filename):
    with open(filename, 'r') as f:
        data = load(f, Loader=Loader)

    return data
