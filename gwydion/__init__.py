__version__ = '0.1dev'

from gwydion.funcs.exponential import Exponential
from gwydion.funcs.linear import Linear
from gwydion.funcs.logarithm import Logarithm
from gwydion.funcs.polynomial import Polynomial, Quadratic, Cubic
from gwydion.funcs.sine import Sine

from gwydion.stats.normal import Normal
from gwydion.stats.poisson import Poisson
from gwydion.stats.hypergeometric import Hypergeometric
from gwydion.stats.binomial import Binomial

from .random_array import RandomArray

__all__ = ['Cubic', 'Exponential', 'Linear', 'Logarithm', 'Polynomial',
           'Quadratic', 'RandomArray', 'Sine', 'Normal',
           'Poisson', "Hypergeometric", "Binomial"]
