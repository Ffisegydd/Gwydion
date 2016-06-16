from scipy.stats import gamma

from gwydion.base import np, Base, ProbDist, DiscreteProbDist
from gwydion.exceptions import GwydionError


class Gamma(ProbDist, Base):
    """
    Gamma function. Returned function is

        y = (x**k-1 * exp(-x/theta))/(theta**k * Gamma(k))

    where Gamma is the Gamma function.

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    k : Float, integer, or None.
        Shape parameter. If none, defaults to a random value between 0 and 10.
    theta : Float, integer, or None.
        Scale parameter. If none, defaults to a random value between 0 and 30.
    xlim : Tuple of floats or integers, or None.
        (Min, Max) values for the x-data. If None, defaults to (0, 30).
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 0.02.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Gamma()  # Default params, returns a random poisson distribution.
    >>>> Gamma(N=1000)  # Increase the number of data points.
    >>>> Gamma(k=1, theta=10)  # Setting k=1 returns the Exponential distribution with theta=1/lambda.
    >>>> Gamma(rand_factor=None)  # Turn off randomness.
    >>>> Gamma(seed=1234)  # Seeded RNG.
    """


    def __init__(self, N=100, k=None, theta=None, xlim=None, rand_factor=0.01, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(k, theta)

    def set_variables(self, k, theta):

        if k is not None and not isinstance(k,  int):
            raise GwydionError('Variables must be either int, or None.')

        if theta is not None and not isinstance(theta, (int, float)):
            raise GwydionError('Variables must be either int, or None.')

        defaults = {
            'k': self.random.rand() * 20,
            'theta': self.random.rand() * 2
        }

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

        if self.xlim is None:
            self.xlim = (0, 30 + (self.random.rand()-0.5) * 10)

    def func(self, x):
        return gamma(self.k, scale=self.theta).pdf(x)

    def sample(self, N=None):
        return gamma(self.k, scale=self.theta).rvs(N, random_state=self.random)

    @property
    def mean(self):
        return self.k*self.theta

    @property
    def mode(self):
        if self.k >= 1:
            return (self.k-1) * self.theta

    @property
    def variance(self):
        return self.k * self.theta**2

    @property
    def skewness(self):
        return 2 / (self.k**0.5)
