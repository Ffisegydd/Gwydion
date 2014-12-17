from abc import ABC, abstractmethod
import random

import numpy as np
import matplotlib.pyplot as plt

class Base(ABC):
    """
    Base ABC object to be subclassed in making functions.
    """

    def __init__(self, N, seed, xlim, rand, rand_factor):
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