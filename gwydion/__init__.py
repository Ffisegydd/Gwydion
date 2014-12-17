__version__ = '0.1dev'

from .funcs.linear import Linear
from .funcs.sine import Sine
from .funcs.exponential import Exponential

__all__ = [Exponential, Linear, Sine]