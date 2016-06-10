from gwydion.base import np, Base, ProbDist
from gwydion.exceptions import GwydionError


class Normal(ProbDist, Base):
    """
    Gaussian function. Returned function is

        y = (1/sigma*sqrt(2*pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    mu : Float, integer, or None.
        Position of peak and mean value. If none, defaults to a random value around 0.0.
    sigma : Float, integer, or None.
        Width parameter equal to standard deviation. If None, defaults to a random value around 0.0.
    xlim : Tuple of floats or integers, or None.
        (Min, Max) values for the x-data. If None, defaults to (mu - 5*sigma, mu + 5*sigma).
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 0.02.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Normal()  # Default params, returns a "normal" exponential.
    >>>> Normal(N=1000)  # Increase the number of data points.
    >>>> Normal(mu=1, sigma=0.01)  # Tall, thin peak at x=1.
    >>>> Normal(rand_factor=None)  # Turn off randomness.
    >>>> Normal(seed=1234)  # Seeded RNG.
    """


    def __init__(self, N=100, mu=None, sigma=None, xlim=None, rand_factor=0.02, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(mu, sigma)

    def set_variables(self, mu, sigma):

        for var in [mu, sigma]:
            if var is not None and not isinstance(var, (float, int)):
                raise GwydionError('Variables must be either float, int, or None.')

        defaults = {'mu': (self.random.rand() - 0.5) * 0.5,
                    'sigma': self.random.rand() * 0.5}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

        if self.xlim is None:
            n = 5
            self.xlim = (self.mu - n*self.sigma, self.mu + n*self.sigma)

    def func(self, x):
        mu, sigma = self.mu, self.sigma

        return 1 / (sigma*np.sqrt(2*np.pi)) * np.exp(-(x - mu)**2/(2*sigma**2))

    @property
    def mean(self):
        return self.mu

    @property
    def mode(self):
        return self.mu

    @property
    def median(self):
        return self.mu

    @property
    def variance(self):
        return self.sigma**2

    @property
    def skewness(self):
        return 0
