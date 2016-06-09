from scipy.stats import hypergeom

from gwydion.base import np, Base, DiscreteProbDistBase
from gwydion.exceptions import GwydionError


class Hypergeometric(DiscreteProbDistBase):
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
    rand_factor : Float or integer.
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
    >>>> Hypergeometric(rand_factor=None)  # Turn off randomness.
    >>>> Hypergeometric(seed=1234)  # Seeded RNG.
    """


    def __init__(self, N=100, M=None, m=None, X=None, xlim=None, rand_factor=0.01, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand_factor=rand_factor,
                         seed=seed)

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

    def func(self, x):
        M = self.M
        m = self.m
        X = self.X

        return hypergeom.pmf(x, M, X, m)
