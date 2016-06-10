from scipy.stats import poisson

from gwydion.base import np, Base, ProbDist, DiscreteProbDist
from gwydion.exceptions import GwydionError


class Poisson(DiscreteProbDist, ProbDist, Base):
    """
    Poisson function. Returned function is

        y = (lam**x * e**-lam) / x!

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    lam : Float, integer, or None.
        Expected number of events in an interval. If none, defaults to a random value between 0 and 30.
    xlim : Tuple of floats or integers, or None.
        (Min, Max) values for the x-data. If None, defaults to (mu - 5*sigma, mu + 5*sigma).
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 0.02.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    NOTE
    ----

    The Poisson distribution is a discrete probability distribution, meaning that x can take only integer values.

    If you try to return N values between x0 and x1, but x1-x0 > N, then you will, by definition, have some duplicate x values.

    Gwydion will prevent this by reducing the number N to the maximum possible. This is by design to ensure that all x values are unique.

    Examples
    --------

    >>>> Poisson()  # Default params, returns a random poisson distribution.
    >>>> Poisson(N=1000)  # Increase the number of data points.
    >>>> Poisson(lam=10)  # Setting the number of events expected in an interval to 10.
    >>>> Poisson(rand_factor=None)  # Turn off randomness.
    >>>> Poisson(seed=1234)  # Seeded RNG.
    """


    def __init__(self, N=100, lam=None, xlim=None, rand_factor=0.01, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(lam)

    def set_variables(self, lam):

        for var in [lam]:
            if var is not None and not isinstance(var, (float, int)):
                raise GwydionError('Variables must be either float, int, or None.')

        defaults = {'lam': self.random.rand() * 30}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

        if self.xlim is None:
            self.xlim = (0, self.lam*3)

    def func(self, x):
        lam = self.lam
        return poisson(lam).pmf(x)

    def sample(self, N=None):
        lam = self.lam
        return poisson(lam).rvs(size=N)

    @property
    def mean(self):
        return self.lam

    @property
    def mode(self):
        return int(self.lam)

    @property
    def median(self):
        return int((self.lam + 1/3) - (0.02/self.lam))

    @property
    def variance(self):
        return self.lam

    @property
    def skewness(self):
        return self.lam ** -0.5
