from inspect import getfullargspec

import numpy as np
import random


class _RandomArray(object):

    def __init__(self, shape, lims=(0, 10), seed=None):
        super().__init__()

        if seed is not None:
            np.random.seed(seed)
            random.seed(seed)

        if isinstance(shape, int):
            self.shape = (shape,)
        elif isinstance(shape, (list, tuple)):
            self.shape = shape
        else:
            raise Exception('Shape parameter incorrect. Must be integer (for 1D array) or tuple or lengths (for n-dimensional).')

        self.lims = lims

        if self.lims[0] > self.lims[1]:
            raise Exception('Limits incorrect. Cannot have a minimum value greater than maximum value.')

    @staticmethod
    def interpolate(x, min, max):
        return (x * (max-min)) + min

    @property
    def arr(self):
        arr = np.random.random(self.shape)
        return _RandomArray.interpolate(arr, *self.lims)

    def __str__(self):
        s = '<{s.__class__.__name__} : shape={s.shape}, lims={s.lims}, seed={s.seed}>'
        return s.format(s=self)

    def __repr__(self):
        v = vars(self)
        spec = getfullargspec(self.__class__)

        s = '{}(' + ', '.join(['{}={}'.format(key, val) for key, val in v.items() if key in spec.args]) + ')'

        return s.format(self.__class__.__name__)


def RandomArray(shape, lims=(0, 10), seed=None):
    arr = _RandomArray(shape, lims=lims, seed=seed)

    return arr.arr
