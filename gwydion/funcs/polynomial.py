from gwydion.base import np, Base
from gwydion.exceptions import GwydionError


class Polynomial(Base):
    """
    Polynomial function. Returned function is

        y = a[0] + a[1]*x + a[2]*x**2 + ... + a[n]*x**n

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    a : List of floats or integers, or None
        Parameters for the polynomial. If None, defaults to either a quadratic or cubic with randomish values.
    xlim : Tuple of floats or integers.
        (Min, Max) values for the x-data. Defaults to (-10, 10).
    rand : Float or integer.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 1.0.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Polynomial()  # Default params, returns a "normal" exponential.
    >>>> Polynomial(N=1000)  # Increase the number of data points.
    >>>> Polynomial(a=[0])  # Horizontal line
    >>>> Polynomial(a=[0, 0, 2])  # Simple quadratic.
    >>>> Polynomial(rand=None)  # Turn off randomness.
    >>>> Polynomial(seed=1234)  # Seeded RNG
    """

    def __init__(self, N=100, a=None, xlim=(-10, 10), rand=1.0, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand=rand,
                         seed=seed)

        self.set_variables(a)

    def set_variables(self, a):

        if a is not None and not all(isinstance(val, (int, float)) for val in a):
            raise GwydionError('Polynomial parameters must be sequence of ints or floats.')

        if a is None:
            n = self.random.randint(2, 4)
            self.a = self.random.rand(n) - 0.5
        else:
            self.a = a

        self.params = self.a

    def func(self, x):
        y = sum(v * np.power(x, i) for i, v in enumerate(self.a))
        return y


class Quadratic(Polynomial):
    """
    Quadratic function. Returned function is

        y = a * x**2 + b * x + c

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    a : Float or integer, or None
        Polynomial quadratic term. If None, defaults to a small randomish value.
    b : Float or integer, or None
        Polynomial linear term. If None, defaults to a small randomish value.
    c : Float or integer, or None
        Polynomial constant term. If None, defaults to a small randomish value.
    xlim : Tuple of floats or integers.
        (Min, Max) values for the x-data. Defaults to (-10, 10).
    rand : Boolean.
        Choose whether the y values should have some random numbers added to them. Defaults to True.
    rand : Float or integer.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 1.0.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Quadratic()  # Default params, returns a "normal" exponential.
    >>>> Quadratic(N=1000)  # Increase the number of data points.
    >>>> Quadratic(a=0, b=0, c=0)  # Horizontal line
    >>>> Quadratic(rand=None)  # Turn off randomness.
    >>>> Quadratic(seed=1234)  # Seeded RNG
    """

    def __init__(self, N=100, a=None, b=None, c=None, xlim=(-10, 10), rand=1.0, seed=None):

        args = [c, b, a]
        if all(arg is None for arg in args):
            args = None
        else:
            args = [arg if arg is not None else 0 for arg in args]

        super().__init__(N=N,
                         a=args,
                         xlim=xlim,
                         rand=rand,
                         seed=seed)


class Cubic(Polynomial):
    """
    Cubic function. Returned function is

        y = a + b * x + c * x**2 + d * x**3

    Parameters
    ----------

    N : Integer.
        Length of arrays to be returned via the data method. Defaults to 100.
    a : Float or integer, or None
        Polynomial constant term. If None, defaults to a small randomish value.
    b : Float or integer, or None
        Polynomial linear term. If None, defaults to a small randomish value.
    c : Float or integer, or None
        Polynomial quadratic term. If None, defaults to a small randomish value.
    d : Float or integer, or None
        Polynomial cubic term. If None, defaults to a small randomish value.
    xlim : Tuple of floats or integers.
        (Min, Max) values for the x-data. Defaults to (-10, 10).
    rand : Boolean.
        Choose whether the y values should have some random numbers added to them. Defaults to True.
    rand : Float or integer.
        The amplitude of random numbers added to the y-data. If None, no random data added. Defaults to 5.0.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Cubic()  # Default params, returns a "normal" exponential.
    >>>> Cubic(N=1000)  # Increase the number of data points.
    >>>> Cubic(a=0, b=0, c=0, d=0)  # Horizontal line
    >>>> Cubic(rand=None)  # Turn off randomness.
    >>>> Cubic(seed=1234)  # Seeded RNG
    """

    def __init__(self, N=100, a=None, b=None, c=None, d=None, xlim=(-10, 10), rand=5.0, seed=None):

        args = [d, c, b, a]
        if all(arg is None for arg in args):
            args = None
        else:
            args = [arg if arg is not None else 0 for arg in args]

        super().__init__(N=N,
                         a=args,
                         xlim=xlim,
                         rand=rand,
                         seed=seed)
