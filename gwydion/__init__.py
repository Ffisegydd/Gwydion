__version__ = '0.1dev'

from .funcs.linear import Linear
from .funcs.sine import Sine
from .funcs.exponential import Exponential
from .funcs.polynomial import Polynomial, Quadratic, Cubic

__all__ = [Exponential, Linear, Polynomial, Quadratic, Sine]