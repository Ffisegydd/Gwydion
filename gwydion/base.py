from abc import ABC, abstractmethod
from inspect import getfullargspec

import numpy as np
import matplotlib.pyplot as plt

from gwydion.exceptions import GwydionError

class Base(ABC):
    """
    Base ABC object to be subclassed in making Gwydion classes.

    Cannot be used as a class by itself, must be subclassed.

    Parameters
    ----------
    N : Integer
        Length of arrays to be returned via the data method.
    xlim : Tuple of floats or integers.
        (Min, Max) values for the x-data.
    rand : Boolean.
        Choose whether the y values should have some random numbers added to them. Defaults to True.
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If rand=False, has no use. Defaults to 0.5.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).
    """

    def __init__(self, N, xlim, add_rand, rand_factor, seed):
        super().__init__()

        self.N = N
        self.seed = seed

        try:
            self.random = np.random.RandomState(self.seed)
        except Exception as e:
            raise GwydionError('Setting the random seed has failed.') from e

        self.xlim = xlim
        self.add_rand = add_rand
        self.rand_factor = rand_factor if self.add_rand else 0

    @property
    def r(self):
        try:
            rand = self.rand_factor * (2 * self.random.rand(self.N) - 1)
        except Exception as e:
            raise GwydionError('Unable to create randomised data.') from e

        return rand

    @property
    def data(self):
        try:
            x = np.linspace(*self.xlim, num=self.N)
        except Exception as e:
            raise GwydionError('Unable to create x-data.') from e

        try:
            y = self.func(x)
        except Exception as e:
            raise GwydionError('Unable to create y-data.') from e

        r = self.r

        return x, y + r

    def plot(self, *args, ax=None, **kwargs):
        x, y = self.data

        if ax is None:
            fig, ax = plt.subplots()

        ax.plot(x, y, *args, **kwargs)

        return ax

    @abstractmethod
    def set_variables(self):
        pass

    @abstractmethod
    def func(self):
        pass

    def __str__(self):
        s = '<{s.__class__.__name__} : N={s.N}, add_rand={s.add_rand}, rand_factor={s.rand_factor}>'
        return s.format(s=self)

    def __repr__(self):
        v = vars(self)
        spec = getfullargspec(self.__class__)

        s = '{}(' + ', '.join(['{}={}'.format(key, val) for key, val in v.items() if key in spec.args]) + ')'

        return s.format(self.__class__.__name__)