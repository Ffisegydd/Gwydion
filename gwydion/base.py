from abc import ABC, abstractmethod

import numpy as np
import matplotlib.pyplot as plt

class Base(ABC):
    """Base ABC object to be subclassed in making functions.
    """

    def __init__(self, N, seed, xlim, rand_func, rand_factor):
        super().__init__()

        self.N = N

        if seed is not None:
            np.random.seed(seed)

        self.xlim = xlim

        self._random_functions = dict(linear=np.random.random,
                                      normal=np.random.randn)

        if isinstance(rand_func, str):
            self.rand_func = self._random_functions[rand_func]
        else:
            self.rand_func = rand_func

        self.rand_factor = rand_factor

    @property
    def r(self):
        return self.rand_factor*((2*self.rand_func(self.N)) - 1) + 1

    @abstractmethod
    def data(self):
        pass

    @abstractmethod
    def func(self):
        pass

    def plot(self, *args, **kwargs):
        x, y = self.data

        fig, ax = plt.subplots()
        ax.plot(x, y, *args, **kwargs)

        return ax