from .base import Base, np, plt

class Linear(Base):
    def __init__(self, N=100, m=None, c=None, xlim=(0,10), rand_func='linear', rand_factor=0.05, seed=None):
        super().__init__(N, seed, xlim, rand_func, rand_factor)

        # Make these more random later.
        if m is None:
            self.m = 0.5
        else:
            self.m = m

        if c is None:
            self.c = 0
        else:
            self.c = c


    @property
    def data(self):
        x = np.linspace(*self.xlim, num=self.N)
        y = x * self.m + self.c
        r = self.r
        return (x, y*r)