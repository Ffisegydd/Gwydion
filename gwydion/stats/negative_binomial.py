from scipy.stats import nbinom

from gwydion.base import np, Base, ProbDist, DiscreteProbDist
from gwydion.exceptions import GwydionError


class NegativeBinomial(DiscreteProbDist):
    """
    NegativeBinomial function. Returned function is

        y = BinomCoeff(x + r - 1, x) * p**k * (1-p) ** (r)

    where BinomCoeff is the binomial coefficient.

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    p : Float, integer, or None.
        Probability of an individual Bernoulli trial succeeding. If none, defaults to a random value between 0 and 30.
    n : Integer, or None.
        Number of successes that must have occurred. If none, defaults to a random value between 0 and 30.
    xlim : Tuple of floats or integers, or None.
        (Min, Max) values for the x-data. If None, defaults to (0, 30).
    rand : Float or integer.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 0.02.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    NOTE
    ----

    The NegativeBinomial distribution is a discrete probability distribution, meaning that x can take only integer values.

    If you try to return N values between x0 and x1, but x1-x0 > N, then you will, by definition, have some duplicate x values.

    Gwydion will prevent this by reducing the number N to the maximum possible. This is by design to ensure that all x values are unique.

    Examples
    --------

    >>>> NegativeBinomial()  # Default params, returns a random poisson distribution.
    >>>> NegativeBinomial(N=1000)  # Increase the number of data points.
    >>>> NegativeBinomial(n=1000, p=0.05)  # A large number of low probability trials.
    >>>> NegativeBinomial(rand=None)  # Turn off randomness.
    >>>> NegativeBinomial(seed=1234)  # Seeded RNG.
    """


    def __init__(self, N=100, n=None, p=None, xlim=None, rand=0.01, seed=None, allow_negative_y=True):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         seed=seed,
                         allow_negative_y=allow_negative_y)

        self.set_variables(n, p)

    def set_variables(self, n, p):


        for var in [n, p]:
            if var is not None and not isinstance(var, (int, float)):
                raise GwydionError('Variables must be either float, int, or None.')

        defaults = {
            'n': self.random.random_integers(1, 8),
            'p': self.random.uniform(0.1, 0.9)
        }

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

        if self.xlim is None:
            self.xlim = (0, 30)
        if self.N > (self.xlim[1]-self.xlim[0]):
            self.N = 1 + self.xlim[1] - self.xlim[0]

    def func(self, x):
        return nbinom(self.n, self.p).pmf(x)

    def sample(self, N=None):
        return nbinom(self.n, self.p).rvs(N, random_state=self.random)

    @property
    def mean(self):
        return (1 - self.p)*self.n/self.p

    @property
    def mode(self):
        return int(self.p*(self.n - 1) / (1 - self.p)) if r > 1 else 0

    @property
    def variance(self):
        return self.p * self.n / (1 - self.p)**2

    @property
    def skewness(self):
        return self.p * self.n / (self.p*self.n)**0.5
