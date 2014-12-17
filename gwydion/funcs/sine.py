from .base import random, np, Base


class Sine(Base):
    """
    Sine wave function. Returned function is

        y = a*sin(b*x + c) + d

    Parameters
    ----------
    N : Integer
        Length of arrays to be returned via the data method. Defaults to 100.
    a : Float, integer, or None.
        Amplitude of the sine wave. If None, defaults to a random value around 1.0.
    b : Float, integer, or None.
        Angular frequency of sine wave. If None, defaults to a random value around 2pi
    c : Float, integer, or None.
        Phase of sine wave. If None, defaults to a random value around 0.0.
    d : Float, integer, or None.
        Offset of sine wave. If None, defaults to a random value around 0.0.
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

    >>>> sin = Sine()  # Default params.
    >>>> sin = Sine(N=1000)  # Increase the number of data points.
    >>>> sin = Sine(a=0.1, d=1.0)  # Modify the function parameters.
    >>>> sin = Sine(rand=False)  # Turn off randomness.
    >>>> sin = Sine(seed=1234)  # Seeded RNG

    """

    def __init__(self, N=100, a=None, b=None, c=None, d=None, xlim=(-10, 10), rand=True, rand_factor=0.1, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(a, b, c, d)

    def set_variables(self, a, b, c, d):

        defaults = {'a': 1.0 + (random.random() - 0.5) * 0.5,
                    'b': 2.0 * np.pi * (random.random() + 0.5),
                    'c': (random.random() - 0.5) * 0.5,
                    'd': random.random() - 0.5}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

    def func(self, x):
        a, b, c, d = self.a, self.b, self.c, self.d

        return a * np.sin(b * x + c) + d
