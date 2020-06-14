'''
A module with errors used for PyDeepMerge
'''


class DeepMergeError(Exception):
    'An abstract base class for errors produced by this package'


class ParserNotAvailableError(DeepMergeError):
    '''
    An error raised when a file does not have
    an appropriate parser to read it currently installed
    '''


class FileTypeError(DeepMergeError):
    '''
    Error raised when file has no file type extension
    '''
