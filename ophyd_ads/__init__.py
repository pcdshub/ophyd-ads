from ._version import get_versions
from .ads import Plc, Symbol, get_connection
from .signal import AdsSignal
from .util import make_address, parse_address

__version__ = get_versions()['version']
del get_versions


__all__ = [
    'AdsSignal',
    'Plc',
    'Symbol',
    'get_connection',
    'make_address',
    'parse_address',
]
