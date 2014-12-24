from gwydion.funcs.base import np, Base


class Gaussian(Base):
    """
    Gaussian function. Returned function is

        y = a * np.exp(-(x - b)**2 / (2 * c**2)) + d

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    a : Float, integer, or None.
        Amplitude of function. If None, defaults to a random value around 1.0.
    b : Float, integer, or None.
        Position of peak. If none, defaults to a random value around 0.0.
    c : Float, integer, or None.
        Width parameter. If None, defaults to a random value around 0.0.
    d : Float, integer, or None.
        y offset. If None, defaults to a random value around 0.0.
    xlim : Tuple of floats or integers, or None.
        (Min, Max) values for the x-data. If None, defaults to (b - 5*c, b + 5*x).
    rand : Boolean.
        Choose whether the y values should have some random numbers added to them. Defaults to True.
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If rand=False, has no use. Defaults to 0.02.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Gaussian()  # Default params, returns a "normal" exponential.
    >>>> Gaussian(N=1000)  # Increase the number of data points.
    >>>> Gaussian(a=100, b=0, c=0.01)  # Tall, thin peak at x=0
    >>>> Gaussian(rand=False)  # Turn off randomness.
    >>>> Gaussian(seed=1234)  # Seeded RNG
    """


    def __init__(self, N=100, a=None, b=None, c=None, d=None, xlim=None, add_rand=True, rand_factor=0.02, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         add_rand=add_rand,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(a, b, c, d)

    def set_variables(self, a, b, c, d):
        defaults = {'a': 1.0 + (self.random.rand() - 0.5) * 0.5,
                    'b': (self.random.rand() - 0.5) * 0.5,
                    'c': self.random.rand() * 0.5,
                    'd': (self.random.rand() - 0.5) * 0.2}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

        if self.xlim is None:
            n = 5
            self.xlim = (self.b - n*self.c, self.b + n*self.c)

    def func(self, x):
        a, b, c, d = self.a, self.b, self.c, self.d

        return a * np.exp(-(x - b)**2/(2*c**2)) + d


class Normal(Gaussian):
    """
    Normal function. Returned function is

        y = (1/sigma*sqrt(2*pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    mu : Float, integer, or None.
        Position of peak. If None, defaults to a random value around 0.0.
    b : Float, integer, or None.
        Width parameter for peak. If none, defaults to a random value close to the standard normal value.
    xlim : Tuple of floats or integers, or None.
        (Min, Max) values for the x-data. If None, defaults to (b - 5*c, b + 5*x).
    rand : Boolean.
        Choose whether the y values should have some random numbers added to them. Defaults to True.
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If rand=False, has no use. Defaults to 0.02.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Normal()  # Default params, returns a "normal" exponential.
    >>>> Normal(N=1000)  # Increase the number of data points.
    >>>> Normal(mu=100, sigma=0.1)  # Tall, thin peak at x=0
    >>>> Normal(rand=False)  # Turn off randomness.
    >>>> Normal(seed=1234)  # Seeded RNG
    """

    def __init__(self, N=100, mu=None, sigma=None, xlim=None, add_rand=True, rand_factor=0.02, seed=None):

        a = 1 / (sigma*np.sqrt(2*np.pi)) if sigma is not None else None
        b = mu
        c = sigma
        d = 0

        super().__init__(N=N, a=a, b=b, c=c, d=d, xlim=xlim, add_rand=add_rand, rand_factor=rand_factor, seed=seed)