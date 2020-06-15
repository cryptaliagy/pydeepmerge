import pkg_resources
import logging


def load_parsers():
    parsers = {}

    for entry_point in pkg_resources.iter_entry_points('pydeepmerge.config_parsers'):
        logging.debug('Found entry_point for %s', entry_point.name)
        try:
            entry_point.require()
            parsers[entry_point.name] = entry_point.load()
        except pkg_resources.DistributionNotFound:
            pass

    return parsers
