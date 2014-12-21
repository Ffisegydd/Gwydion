__version__ = '0.1dev'

import numpy as np

from .funcs.linear import Linear
from .funcs.sine import Sine
from .funcs.exponential import Exponential
from .funcs.polynomial import Polynomial, Quadratic, Cubic
from .funcs.logarithm import Logarithm

from array import RandomArray

__all__ = [RandomArray, Exponential, Linear, Logarithm, Polynomial, Quadratic, Sine]