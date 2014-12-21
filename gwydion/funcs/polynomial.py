from .base import np, Base


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
    rand : Boolean.
        Choose whether the y values should have some random numbers added to them. Defaults to True.
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If rand=False, has no use. Defaults to 0.1.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Polynomial()  # Default params, returns a "normal" exponential.
    >>>> Polynomial(N=1000)  # Increase the number of data points.
    >>>> Polynomial(a=[0])  # Horizontal line
    >>>> Polynomial(a=[0, 0, 2])  # Simple quadratic.
    >>>> Polynomial(rand=False)  # Turn off randomness.
    >>>> Polynomial(seed=1234)  # Seeded RNG
    """

    def __init__(self, N=100, a=None, xlim=(-10, 10), add_rand=True, rand_factor=1.0, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         add_rand=add_rand,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(a)

    def set_variables(self, a):

        if a is None:
            n = self.random.randint(2, 4)
            # self.a = [(random.random() - 0.5) for _ in range(n)]
            self.a = self.random.rand(n) - 0.5
        else:
            self.a = a

        self.params = self.a

    def func(self, x):
        y = sum([v * np.power(x, i) for i, v in enumerate(self.a)])
        return y


class Quadratic(Polynomial):
    """
    Quadratic function. Returned function is

        y = a + b * x + c * x**2

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
    xlim : Tuple of floats or integers.
        (Min, Max) values for the x-data. Defaults to (-10, 10).
    rand : Boolean.
        Choose whether the y values should have some random numbers added to them. Defaults to True.
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If rand=False, has no use. Defaults to 0.1.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Quadratic()  # Default params, returns a "normal" exponential.
    >>>> Quadratic(N=1000)  # Increase the number of data points.
    >>>> Quadratic(a=0, b=0, c=0)  # Horizontal line
    >>>> Quadratic(rand=False)  # Turn off randomness.
    >>>> Quadratic(seed=1234)  # Seeded RNG
    """

    def __init__(self, N=100, a=None, b=None, c=None, xlim=(-10, 10), add_rand=True, rand_factor=1.0, seed=None):

        args = [i for i in [a, b, c] if i is not None] or None

        super().__init__(N=N,
                         a=args,
                         xlim=xlim,
                         add_rand=add_rand,
                         rand_factor=rand_factor,
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
    rand_factor : Float or integer.
        The amplitude of random numbers added to the y-data. If rand=False, has no use. Defaults to 0.1.
    seed : Integer or None.
        Used to seed the RNG if repeatable results are required. Defaults to None (and thus no seeding).

    Examples
    --------

    >>>> Cubic()  # Default params, returns a "normal" exponential.
    >>>> Cubic(N=1000)  # Increase the number of data points.
    >>>> Cubic(a=0, b=0, c=0, d=0)  # Horizontal line
    >>>> Cubic(rand=False)  # Turn off randomness.
    >>>> Cubic(seed=1234)  # Seeded RNG
    """

    def __init__(self, N=100, a=None, b=None, c=None, d=None, xlim=(-10, 10), add_rand=True, rand_factor=5.0, seed=None):

        args = [i for i in [a, b, c, d] if i is not None] or None

        print(vars(self))

        super().__init__(N=N,
                         a=args,
                         xlim=xlim,
                         add_rand=add_rand,
                         rand_factor=rand_factor,
                         seed=seed)