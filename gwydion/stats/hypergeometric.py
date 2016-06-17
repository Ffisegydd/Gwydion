from scipy.stats import hypergeom

from gwydion.base import np, Base, ProbDist, DiscreteProbDist
from gwydion.exceptions import GwydionError


class Hypergeometric(DiscreteProbDist):
    """
    Hypergeometric function. Returned function is

        y = BinomCoeff(X, x) * BinomCoeff(M-X, m-x) / BinomCoeff(M, m)

    where BinomCoeff is the binomial coefficient.

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    M : Integer, or None.
        Population size. If none, defaults to a random value between 0 and 30.
    X : Integer, or None.
        Number of success states in the population. If none, defaults to a random value between 0 and 30.
    m : Integer, or None.
        Number of events. If none, defaults to a random value between 0 and 30.
    xlim : Tuple of floats or integers, or None.
        (Min, Max) values for the x-data. If None, defaults to (mu - 5*sigma, mu + 5*sigma).
    rand : Float or integer.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 0.02.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    NOTE
    ----

    The Hypergeometric distribution is a discrete probability distribution, meaning that x can take only integer values.

    If you try to return N values between x0 and x1, but x1-x0 > N, then you will, by definition, have some duplicate x values.

    Gwydion will prevent this by reducing the number N to the maximum possible. This is by design to ensure that all x values are unique.

    Examples
    --------

    >>>> Hypergeometric()  # Default params, returns a random poisson distribution.
    >>>> Hypergeometric(N=1000)  # Increase the number of data points.
    >>>> Hypergeometric(M=100, X=50)  # Setting the population and success sizes to 100 and 50, respectively.
    >>>> Hypergeometric(rand=None)  # Turn off randomness.
    >>>> Hypergeometric(seed=1234)  # Seeded RNG.
    """


    def __init__(self, N=100, M=None, m=None, X=None, xlim=None, rand=0.01, seed=None, allow_negative_y=True):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         seed=seed,
                         allow_negative_y=allow_negative_y)

        self.set_variables(M, m, X)

    def set_variables(self, M, m, X):

        for var in [M, m, X]:
            if var is not None and not isinstance(var,  int):
                raise GwydionError('Variables must be either int, or None.')

        defaults = {
            'M': self.random.random_integers(20, 40),
            'X': self.random.random_integers(10, 19),
            'm': self.random.random_integers(5, 15)
        }

        for key, val in defaults.items():
            if locals()[key] is None:
                setattr(self, key, val)
            else:
                setattr(self, key, locals()[key])

        if self.xlim is None:
            self.xlim = (0, self.m)
        if self.N > (self.xlim[1]-self.xlim[0]):
            self.N = self.xlim[1] - self.xlim[0]

    def func(self, x):
        return hypergeom(self.M, self.X, self.m).pmf(x)

    def sample(self, x=None):
        return hypergeom(self.M, self.X, self.m).rvs(x, random_state=self.random)

    @property
    def mean(self):
        return self.m*self.X/self.M

    @property
    def mode(self):
        return int(((self.m+1)*(self.X+1))/(self.M+2))

    @property
    def variance(self):
        M = self.M
        X = self.X
        m = self.m

        return int(m * (X/M) * ((M-X)/M) * ((M-m)/(M-1)))

    @property
    def skewness(self):
        M = self.M
        X = self.X
        m = self.m

        return int(((M - 2*X) * ((M-1)**0.5)*(M - 2*m))/((M-2) * (m * X * (M-X) * (M-m))**0.5))
