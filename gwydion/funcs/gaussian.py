from .base import random, np, plt, Base

class Gaussian(Base):

    def __init__(self, N=100, a=None, b=None, c=None, d=None, xlim=None, rand=True, rand_factor=0.02, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(a, b, c, d, n_xlim=5)

    def set_variables(self, a, b, c, d, n_xlim):
        defaults = {'a': 1.0 + (random.random() - 0.5) * 0.5,
                    'b': (random.random() - 0.5) * 0.5,
                    'c': (random.random() - 0.5) * 0.5,
                    'd': (random.random() - 0.5) * 0.2}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

        if self.xlim is None:
            self.xlim = (self.b - n_xlim*self.c, self.b + n_xlim*self.c)

    def func(self, x):
        a, b, c, d = self.a, self.b, self.c, self.d

        return a * np.exp(-(x - b)**2/(2*c**2)) + d


class Normal(Gaussian):

    def __init__(self, N=100, mu=None, sigma=None, xlim=None, rand=True, rand_factor=0.02, seed=None):

        a = 1 / (sigma*np.sqrt(2*np.pi)) if sigma is not None else None
        b = mu
        c = sigma
        d = 0

        super().__init__(N=N, a=a, b=b, c=c, d=d, xlim=xlim, rand=rand, rand_factor=rand_factor, seed=seed)