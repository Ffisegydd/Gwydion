from math import ceil, log2

from scipy.stats import geom

from gwydion.base import np, Base, ProbDist, DiscreteProbDist
from gwydion.exceptions import GwydionError


class Geometric(DiscreteProbDist, ProbDist, Base):
    """
    Geometric function. Returned function is

        y = p*(1 - p)**(x-1)

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    p : Float, integer, or None.
        Probability of each trial succeeding. If none, defaults to a random value between 0 and 30.
    xlim : Tuple of floats or integers, or None.
        (Min, Max) values for the x-data. If None, defaults to (mu - 5*sigma, mu + 5*sigma).
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 0.02.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    NOTE
    ----

    The Geometric distribution is a discrete probability distribution, meaning that x can take only integer values.

    If you try to return N values between x0 and x1, but x1-x0 > N, then you will, by definition, have some duplicate x values.

    Gwydion will prevent this by reducing the number N to the maximum possible. This is by design to ensure that all x values are unique.

    Examples
    --------

    >>>> Geometric()  # Default params, returns a random geom distribution.
    >>>> Geometric(N=1000)  # Increase the number of data points.
    >>>> Geometric(p=10)  # Setting the number of events expected in an interval to 10.
    >>>> Geometric(rand_factor=None)  # Turn off randomness.
    >>>> Geometric(seed=1234)  # Seeded RNG.
    """


    def __init__(self, N=100, p=None, xlim=None, rand_factor=0.01, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(p)

    def set_variables(self, p):

        for var in [p]:
            if var is not None and not isinstance(var, (float, int)):
                raise GwydionError('Variables must be either float, int, or None.')

        defaults = {'p': self.random.uniform(0.1,0.9)}

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

        if self.xlim is None:
            self.xlim = (0, ceil(5/self.p))
        if self.N > (self.xlim[1]-self.xlim[0]):
            self.N = self.xlim[1] - self.xlim[0]

    def func(self, x):
        p = self.p
        return geom(p).pmf(x)

    def sample(self, N=None):
        p = self.p
        return geom(p).rvs(size=N, random_state=self.random)

    @property
    def mean(self):
        return 1/self.p

    @property
    def median(self):
        return ceil((-1 / (log2(1 - self.p))))

    @property
    def mode(self):
        return 1

    @property
    def variance(self):
        return (1 - self.p) / self.p**2

    @property
    def skewness(self):
        return (2 - self.p) / (1 - self.p)**0.5
