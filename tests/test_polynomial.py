import pytest
import numpy as np

from gwydion import Polynomial, Quadratic, Cubic
from gwydion.exceptions import GwydionError


SEED = 31415927
TOLERANCE = 0.00001

def test_polynomial_creation():
    polynomial = Polynomial()
    assert polynomial


def test_polynomial_non_random():
    polynomial = Polynomial(rand=None, a=[0, 1, 2] , xlim=(-3, 3), N=7)
    x, y = polynomial.data

    for i, j in zip(x, [-3, -2, -1, 0, 1, 2, 3]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, [15., 6., 1., 0., 3., 10., 21.]):
        assert abs(i - j) < TOLERANCE


def test_polynomial_random():
    x_test = [-3, -2, -1, 0, 1, 2, 3]
    y_test = [-0.3713085, 0.38057779, 0.28028819, 0.99593501, 0.57225677, 1.61515779, 1.99664164]

    polynomial = Polynomial(seed=SEED, N=7, xlim=(-3, 3))
    x, y = polynomial.data

    for i, j in zip(polynomial.a, [0.13858659, 0.35275832]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_polynomial_printing():
    polynomial = Polynomial(seed=SEED, N=11)
    for s in ['N=11', 'rand=1.0']:
        assert s in str(polynomial)

    for s in ['N=11', 'xlim=(-10, 10)', 'seed=31415927', 'a=[ 0.13858659  0.35275832]', 'rand=1.0']:
        assert s in repr(polynomial)


def test_polynomial_seeding():
    polynomial1 = Polynomial(seed=SEED, xlim=(1,10))
    polynomial2 = Polynomial(seed=SEED, xlim=(1,10))

    assert polynomial1 != polynomial2
    for i, j in zip(polynomial1.a, polynomial2.a):
        assert abs(i - j) < TOLERANCE

    assert all(np.array_equal(i, j) for i, j in zip(polynomial1.data, polynomial2.data))


def test_polynomial_exceptions():
    with pytest.raises(GwydionError):
        Polynomial(a=[2j, 3j])
    with pytest.raises(GwydionError):
        Polynomial(a='1234')


def test_quadratic_creation():
    quadratic = Quadratic()
    assert quadratic


def test_quadratic_non_random():
    quadratic = Quadratic(rand=None, a=2, b=1, c=0, xlim=(-3, 3), N=7)
    polynomial = Polynomial(rand=None, a=[0, 1, 2], xlim=(-3, 3), N=7)

    for u, v in zip(quadratic.data, polynomial.data):
        for i, j in zip(u, v):
            assert abs(i - j) < TOLERANCE


def test_quadratic_random():
    x_test = [-3, -2, -1, 0, 1, 2, 3]
    y_test = [-0.3713085, 0.38057779, 0.28028819, 0.99593501, 0.57225677, 1.61515779, 1.99664164]

    quadratic = Quadratic(seed=SEED, N=7, xlim=(-3, 3))
    x, y = quadratic.data

    for i, j in zip(quadratic.a, [0.13858659, 0.35275832]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_quadratic_printing():
    quadratic = Quadratic(seed=SEED, N=11)
    for s in ['N=11', 'rand=1.0']:
        assert s in str(quadratic)

    for s in ['N=11', 'xlim=(-10, 10)', 'seed=31415927', 'a=[ 0.13858659  0.35275832]', 'rand=1.0']:
        assert s in repr(quadratic)


def test_quadratic_seeding():
    quadratic1 = Quadratic(seed=SEED, xlim=(1,10))
    quadratic2 = Quadratic(seed=SEED, xlim=(1,10))

    assert quadratic1 != quadratic2
    for i, j in zip(quadratic1.a, quadratic2.a):
        assert abs(i - j) < TOLERANCE


    assert all(np.array_equal(i, j) for i, j in zip(quadratic1.data, quadratic2.data))

def test_quadratic_exceptions():
    with pytest.raises(GwydionError):
        Quadratic(a=2j, b=3j)
    with pytest.raises(GwydionError):
        Quadratic(a='1234')


def test_cubic_creation():
    cubic = Cubic()
    assert cubic


def test_cubic_non_random():
    cubic = Cubic(rand=None, a=2, b=1, c=0, d=-1, xlim=(-3, 3), N=7)
    polynomial = Polynomial(rand=None, a=[-1, 0, 1, 2], xlim=(-3, 3), N=7)

    for u, v in zip(cubic.data, polynomial.data):
        for i, j in zip(u, v):
            assert abs(i - j) < TOLERANCE


def test_cubic_random():
    x_test = [-3, -2, -1, 0, 1, 2, 3]
    y_test = [1.82221094, 4.1706091, 2.25812782, 4.4253287, 0.89590419, 4.69937605, 5.19576204]

    cubic = Cubic(seed=SEED, N=7, xlim=(-3, 3))
    x, y = cubic.data

    for i, j in zip(cubic.a, [0.13858659, 0.35275832]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_cubic_printing():
    cubic = Cubic(seed=SEED, N=11)
    for s in ['N=11', 'rand=5.0']:
        assert s in str(cubic)

    for s in ['N=11', 'xlim=(-10, 10)', 'seed=31415927', 'a=[ 0.13858659  0.35275832]', 'rand=5.0']:
        assert s in repr(cubic)


def test_cubic_seeding():
    cubic1 = Cubic(seed=SEED, xlim=(1,10))
    cubic2 = Cubic(seed=SEED, xlim=(1,10))

    assert cubic1 != cubic2
    for i, j in zip(cubic1.a, cubic2.a):
        assert abs(i - j) < TOLERANCE

    assert all(np.array_equal(i, j) for i, j in zip(cubic1.data, cubic2.data))

def test_cubic_exceptions():
    with pytest.raises(GwydionError):
        Cubic(a=2j, b=3j)
    with pytest.raises(GwydionError):
        Cubic(a='1234')