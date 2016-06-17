from abc import ABC, abstractmethod
from inspect import getfullargspec

import numpy as np
try:
    import scipy.integrate as si
except ImportError:
    pass
import matplotlib.pyplot as plt

from copy import deepcopy

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
    rand : Float or integer.
        The amplitude of random numbers added to the y-data. If rand=False, has no use. Defaults to 0.5.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).
    """

    def __init__(self, N, xlim, rand, seed):
        super().__init__()

        self.N = N
        self.seed = seed
        self._x = None
        self._y = None
        self._r = None
        self._data = None

        try:
            self.random = np.random.RandomState(self.seed)
        except Exception as e:
            raise GwydionError('Setting the random seed has failed.') from e

        self.xlim = xlim
        self.rand = rand if rand is not None else 0

    @property
    def r(self):
        if self._r is None:
            try:
                self._r = self.rand * (2 * self.random.rand(self.N) - 1)
            except Exception as e:
                raise GwydionError('Unable to create randomised data.') from e

        return self._r

    @property
    def x(self):
        if self._x is None:
            try:
                self._x = np.linspace(*self.xlim, num=self.N)
            except Exception as e:
                raise GwydionError('Unable to create x-data.') from e

        return self._x

    @property
    def y(self):
        if self._y is None:
            try:
                self._y = self.func(self.x)
            except Exception as e:
                raise GwydionError('Unable to create y-data.') from e

        return self._y + self.r

    @property
    def data(self):
        return self.x, self.y

    def plot(self, *args, ax=None, **kwargs):
        x, y = self.data

        if ax is None:
            fig, ax = plt.subplots()

        ax.plot(x, y, *args, **kwargs)

        return ax

    @abstractmethod
    def set_variables(self, *args):
        pass

    @abstractmethod
    def func(self):
        pass

    def __str__(self):
        s = '<{s.__class__.__name__} : N={s.N}, rand={s.rand}>'
        return s.format(s=self)

    def __repr__(self):
        v = vars(self)
        spec = getfullargspec(self.__class__)

        s = '{}(' + ', '.join(['{}={}'.format(key, val) for key, val in v.items() if key in spec.args]) + ')'

        return s.format(self.__class__.__name__)

    def __setattr__(self, name, value):
        if name not in {'r', 'x', 'y', '_r', '_x', '_y'}:
            super().__setattr__('_x', None)
            super().__setattr__('_y', None)
            super().__setattr__('_r', None)

        super().__setattr__(name, value)


class ProbDist(Base):

    def __init__(self, N, xlim, rand, seed, allow_negative_y=True):
        self.allow_negative_y = allow_negative_y

        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         seed=seed)

    @property
    def y(self):
        if self._y is None:
            try:
                self._y = self.func(self.x)
            except Exception as e:
                raise GwydionError('Unable to create y-data.') from e

        y = self._y + self.r
        if not self.allow_negative_y:
            y[y<0] = 0

        return y

    def to_cum(self):
        new = deepcopy(self)
        new._y = si.cumtrapz(new.y, new.x, initial=0)
        return new

    def sample(self, N):
        return NotImplemented()

    @property
    def mean(self):
        return NotImplemented()

    @property
    def mode(self):
        return NotImplemented()

    @property
    def median(self):
        return NotImplemented()

    @property
    def variance(self):
        return NotImplemented()

    @property
    def skewness(self):
        return NotImplemented()


class DiscreteProbDist(ProbDist):

    @property
    def x(self):
        if self._x is None:
            try:
                self._x = np.unique(np.linspace(*self.xlim, num=self.N).astype('int'))
            except Exception as e:
                raise GwydionError('Unable to create x-data.') from e

        return self._x
