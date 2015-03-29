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
    polynomial = Polynomial(rand_factor=None, a=[0, 1, 2] , xlim=(-3, 3), N=7)
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
    print(polynomial.a)

    for i, j in zip(polynomial.a, [0.13858659, 0.35275832]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_polynomial_printing():
    polynomial = Polynomial(seed=SEED, N=11)
    print(str(polynomial))
    print(repr(polynomial))
    for s in ['N=11', 'rand_factor=1.0']:
        assert s in str(polynomial)

    for s in ['N=11', 'xlim=(-10, 10)', 'seed=31415927', 'a=[ 0.13858659  0.35275832]', 'rand_factor=1.0']:
        assert s in repr(polynomial)


def test_polynomial_seeding():
    polynomial1 = Polynomial(seed=SEED, xlim=(1,10))
    polynomial2 = Polynomial(seed=SEED, xlim=(1,10))

    assert polynomial1 != polynomial2
    for i, j in zip(polynomial1.a, polynomial2.a):
        assert abs(i - j) < TOLERANCE

    print(polynomial1.data, polynomial2.data)

    assert all(np.array_equal(i, j) for i, j in zip(polynomial1.data, polynomial2.data))

def test_polynomial_exceptions():
    with pytest.raises(GwydionError):
        Polynomial(a=[2j, 3j])
    with pytest.raises(GwydionError):
        Polynomial(a='1234')

