from .base import random, np, plt, Base


class Polynomial(Base):
    """
    Polynomail function. Returned function is

        y = a[0] + a[1]*x + a[2]*x**2 + ... + a[n]*x**n

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    a : List of floats or integers, or None
        Parameters for the polynomial. If None, defaults to either a quadratic or cubic with randomish values.
    xlim : Tuple of floats or integers.
        (Min, Max) values for the x-data. Defaults to (-10, 10).
    rand : Boolean.
        Choose whether the y values should have some random numbers added to them. Defaults to True.
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If rand=False, has no use. Defaults to 0.1.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> poly = Polynomial()  # Default params, returns a "normal" exponential.
    >>>> poly = Polynomial(N=1000)  # Increase the number of data points.
    >>>> poly = Polynomial(a=[0])  # Horizontal line
    >>>> poly = Polynomial(a=[0, 0, 2])  # Simple quadratic.
    >>>> poly = Polynomial(rand=False)  # Turn off randomness.
    >>>> poly = Polynomial(seed=1234)  # Seeded RNG
    """

    def __init__(self, N=100, a=None, xlim=(-10, 10), rand=True, rand_factor=1.0, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(a)

    def set_variables(self, a):

        if a is None:
            n = random.randint(2, 3)
            self.a = [(random.random() - 0.5) for _ in range(n)]
        else:
            self.a = a

        self.params = self.a

    def func(self, x):
        y = sum([v * np.power(x, i) for i, v in enumerate(self.a)])
        return y


class Quadratic(Polynomial):
    def __init__(self, N=100, a=None, b=None, c=None, xlim=(-10, 10), rand=True, rand_factor=1.0, seed=None):

        self.set_quad_variables(a, b, c)

        super().__init__(N=N,
                         a=[self.a, self.b, self.c],
                         xlim=xlim,
                         rand=rand,
                         rand_factor=rand_factor,
                         seed=seed)

        del self.b
        del self.c

    def set_quad_variables(self, a, b, c):
        defaults = {'a': (random.random() - 0.5) * 0.5,
                    'b': (random.random() - 0.5) * 0.5,
                    'c': (random.random() - 0.5) * 0.5}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])


class Cubic(Polynomial):
    def __init__(self, N=100, a=None, b=None, c=None, d=None, xlim=(-10, 10), rand=True, rand_factor=5.0, seed=None):

        self.set_cubic_variables(a, b, c, d)

        super().__init__(N=N,
                         a=[self.a, self.b, self.c, self.d],
                         xlim=xlim,
                         rand=rand,
                         rand_factor=rand_factor,
                         seed=seed)

        del self.b
        del self.c
        del self.d

    def set_cubic_variables(self, a, b, c, d):
        defaults = {'a': (random.random() - 0.5) * 0.5,
                    'b': (random.random() - 0.5) * 0.5,
                    'c': (random.random() - 0.5) * 0.5,
                    'd': (random.random() - 0.5) * 0.5}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])