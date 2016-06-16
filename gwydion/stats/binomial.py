from scipy.stats import binom

from gwydion.base import np, Base, ProbDist, DiscreteProbDist
from gwydion.exceptions import GwydionError


class Binomial(DiscreteProbDist, ProbDist, Base):
    """
    Binomial function. Returned function is

        y = BinomCoeff(n, k) * p**k * (1-p) ** (n-k)

    where BinomCoeff is the binomial coefficient.

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    n : Integer, or None.
        Number of trials. If none, defaults to a random value between 0 and 30.
    p : Integer, or None.
        Probability of a single trial being successful. If none, defaults to a random value between 0 and 30.
    xlim : Tuple of floats or integers, or None.
        (Min, Max) values for the x-data. If None, defaults to (mu - 5*sigma, mu + 5*sigma).
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 0.02.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    NOTE
    ----

    The Binomial distribution is a discrete probability distribution, meaning that x can take only integer values.

    If you try to return N values between x0 and x1, but x1-x0 > N, then you will, by definition, have some duplicate x values.

    Gwydion will prevent this by reducing the number N to the maximum possible. This is by design to ensure that all x values are unique.

    Examples
    --------

    >>>> Binomial()  # Default params, returns a random poisson distribution.
    >>>> Binomial(N=1000)  # Increase the number of data points.
    >>>> Binomial(n=1000, p=0.05)  # A large number of low probability trials.
    >>>> Binomial(rand_factor=None)  # Turn off randomness.
    >>>> Binomial(seed=1234)  # Seeded RNG.
    """


    def __init__(self, N=100, n=None, p=None, xlim=None, rand_factor=0.01, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(n, p)

    def set_variables(self, n, p):

        if n is not None and not isinstance(n,  int):
            raise GwydionError('Variables must be either int, or None.')

        if p is not None and not isinstance(p, (int, float)):
            raise GwydionError('Variables must be either int, or None.')

        defaults = {
            'n': self.random.random_integers(10, 50),
            'p': (self.random.rand() + 0.8)/2
        }

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

        if self.xlim is None:
            self.xlim = (0, self.n)
        if self.N > (self.xlim[1]-self.xlim[0]):
            self.N = self.xlim[1] - self.xlim[0]

    def func(self, x):
        return binom(self.n, self.p).pmf(x)

    def sample(self, N=None):
        return binom(self.n, self.p).rvs(N, random_state=self.random)

    @property
    def mean(self):
        return self.n*self.p

    @property
    def median(self):
        return int(self.n * self.p)

    @property
    def mode(self):
        return int((self.n+1)*self.p)

    @property
    def variance(self):
        return self.n*self.p*(1 - self.p)

    @property
    def skewness(self):
        return (1 - 2*self.p) / (self.n * self.p * (1-self.p))**0.5
