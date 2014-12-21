__version__ = '0.1dev'

import numpy as np

from .funcs.exponential import Exponential
from .funcs.linear import Linear
from .funcs.gaussian import Gaussian
from .funcs.logarithm import Logarithm
from .funcs.polynomial import Polynomial, Quadratic, Cubic
from .funcs.sine import Sine

from array import RandomArray

__all__ = [Cubic, Exponential, Gaussian, Linear, Logarithm, Polynomial, Quadratic, RandomArray, Sine]