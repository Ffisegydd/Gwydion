from gwydion.base import np, Base


class Sine(Base):
    """
    Sine wave function. Returned function is

        y = A*sin(2*pi*f*x + p)

    Parameters
    ----------
    N : Integer
        Length of arrays to be returned via the data method. Defaults to 100.
    A : Float, integer, or None.
        Amplitude of the sine wave. If None, defaults to a random value around 1.0.
    f : Float, integer, or None.
        Frequency of sine wave. If None, defaults to a random value around 2pi
    p : Float, integer, or None.
        Phase of sine wave. If None, defaults to a random value around 0.0.
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

    >>>> Sine()  # Default params.
    >>>> Sine(N=1000)  # Increase the number of data points.
    >>>> Sine(A=0.1, p=1.0)  # Modify the function parameters.
    >>>> Sine(rand=False)  # Turn off randomness.
    >>>> Sine(seed=1234)  # Seeded RNG

    """

    def __init__(self, N=100, A=None, f=None, p=None, xlim=(-10, 10), add_rand=True, rand_factor=0.1, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         add_rand=add_rand,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(A, f, p)

    def set_variables(self, A, f, p):

        defaults = {'A': 1.0 + (self.random.rand() - 0.5) * 0.5,
                    'f': self.random.rand() + 0.5,
                    'p': (self.random.rand() - 0.5) * 0.5}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

    def func(self, x):
        A, f, p = self.A, self.f, self.p

        return A * np.sin(2 * np.pi * f * x + p)
