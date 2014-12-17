from .base import random, np, plt, Base

class Logarithm(Base):
    """
    Exponential function (power law). Returned function is

        y = a * log(base)(b*x + c) + d

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    base : Float, integer, or None
        Base for function. If None, defaults to e = 2.718....
    a : Float, integer, or None.
        Amplitude of function. If None, defaults to a random value around 1.0.
    b : Float, integer, or None.
        Amplitude of the argument. If none, defaults to a random value around 0.0.
    c : Float, integer, or None.
        x offset. If None, defaults to a random value around 0.0.
    d : Float, integer, or None.
        y offset. If None, defaults to a random value around 0.0.
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

    >>>> log = Logarithm()  # Default params, returns a "normal" exponential.
    >>>> log = Logarithm(N=1000)  # Increase the number of data points.
    >>>> log = Logarithm(a=2, c=0)  # Exponential decay.
    >>>> log = Logarithm(rand=False)  # Turn off randomness.
    >>>> log = Logarithm(seed=1234)  # Seeded RNG

    """

    def __init__(self, N=100, base=None, a=None, b=None, c=None, d=None, xlim=(-10,10), rand=True, rand_factor=0.1, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(base, a, b, c, d)

    def set_variables(self, base, a, b, c, d):

        defaults = {'base': np.e,
                    'a': 1.0 + (random.random() - 0.5) * 0.5,
                    'b': (random.random() - 0.5) * 0.5,
                    'c': (random.random() - 0.5) * 0.5,
                    'd': (random.random() - 0.5) * 0.5}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

    def func(self, x):
        base, a, b, c, d = self.base, self.a, self.b, self.c, self.d

        return (a*np.log(b*x + c)/np.log(base)) + d