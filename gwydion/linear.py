from .base import random, np, plt, Base

class Linear(Base):
    """Linear function
    """
    def __init__(self, N=100, m=None, c=None, xlim=(0,10), rand_func='linear', rand_factor=0.05, seed=None):
        super().__init__(N, seed, xlim, rand_func, rand_factor)

        self.randomise_variables(m, c)


    def randomise_variables(self, m, c):
        if m is None:
            self.m = (random.random() + 0.5)*2
        else:
            self.m = m

        if c is None:
            self.c = (random.random() - 0.5)*10
        else:
            self.c = c


    def func(self, x, m=None, c=None):
        if m is None:
            m = self.m
        if c is None:
            c = self.c

        return m*x + c


    @property
    def data(self):
        x = np.linspace(*self.xlim, num=self.N)
        y = self.func(x)
        r = self.r
        return (x, y*r)
