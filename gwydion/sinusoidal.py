from .base import random, np, plt, Base

class Sine(Base):
    """
    Sine wave function. Returned function is

        y = a*sin(b*t + c) + d

    Parameters
    ----------

    """


    def __init__(self, N=100, a=None, b=None, c=None, d=None, xlim=(-10, 10), rand=True, rand_factor=0.1, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(a, b, c, d)

    def set_variables(self, a, b, c, d):

        if a is None:
            self.a = 1.0 + (random.random() - 0.5) * 0.5
        else:
            self.a = a

        if b is None:
            self.b = 2.0*np.pi * (random.random() + 0.5)
        else:
            self.b = b

        if c is None:
            self.c = (random.random() - 0.5) * 0.5
        else:
            self.c = c

        if d is None:
            self.d = random.random() - 0.5
        else:
            self.d = d


    def func(self, x):
        a, b, c, d = self.a, self.b, self.c, self.d

        return a*np.sin(b*x + c) + d
