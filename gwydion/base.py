from abc import ABC, abstractmethod
import random

import numpy as np
import matplotlib.pyplot as plt

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

    def __init__(self, N, xlim, rand, rand_factor, seed):
        super().__init__()

        self.N = N

        if seed is not None:
            np.random.seed(seed)
            random.seed(seed)

        self.xlim = xlim

        self.rand = rand

        if self.rand:
            self.rand_factor = rand_factor
        else:
            self.rand = 0

    @property
    def r(self):

        return self.rand_factor*(2*np.random.random(self.N) - 1)


    @abstractmethod
    def data(self):
        pass

    @abstractmethod
    def func(self):
        pass

    def plot(self, *args, ax=None, **kwargs):
        x, y = self.data

        if ax is None:
            fig, ax = plt.subplots()

        ax.plot(x, y, *args, **kwargs)

        return ax