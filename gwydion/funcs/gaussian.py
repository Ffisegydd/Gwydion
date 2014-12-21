from .base import random, np, plt, Base

class Gaussian(Base):

    def __init__(self, N=1000, a=None, b=None, c=None, d=None, xlim=(-2,2), rand=True, rand_factor=0.02, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(a, b, c, d)

    def set_variables(self, a, b, c, d):
        defaults = {'a': 1.0 + (random.random() - 0.5) * 0.5,
                    'b': (random.random() - 0.5) * 0.5,
                    'c': (random.random() - 0.5) * 0.5,
                    'd': (random.random() - 0.5) * 0.2}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

    def func(self, x):
        a, b, c, d = self.a, self.b, self.c, self.d

        return a * np.exp(-(x - b)**2/(2*c**2)) + d