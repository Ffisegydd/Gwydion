import pytest
import numpy as np

from gwydion import Poisson
from gwydion.exceptions import GwydionError


SEED = 31415927
TOLERANCE = 0.00001

def test_poisson_creation():
    poisson = Poisson()
    assert poisson


def test_poisson_non_random():
    poisson = Poisson(rand_factor=None, lam=2, xlim=(0,10), N=7)
    x, y = poisson.data

    for i, j in zip(x, [0, 1, 3, 5, 6, 8, 10]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, [1.35335283e-01, 2.70670566e-01, 1.80447044e-01, 3.60894089e-02, 1.20298030e-02, 8.59271640e-04, 3.81898506e-05]):
        assert abs(i - j) < TOLERANCE


def test_poisson_random():
    x_test = [0, 1, 3, 5, 6, 8, 10]
    y_test = [0.00634749, 0.0054957, 0.00242271, 0.04049159, 0.05722324, 0.10456898, 0.12780699]

    poisson = Poisson(seed=SEED, N=7, xlim=(0, 10))
    x, y = poisson.data

    assert poisson.lam == 10.398429625910502

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_poisson_variables():

    poisson = Poisson(seed=SEED, N=7, xlim=(-3, 3))

    assert poisson.mean == 10.398429625910502
    assert poisson.median == 10
    assert poisson.mode == 10
    assert poisson.variance == 10.398429625910502
    assert poisson.skewness == 0.31011025029450545


def test_poisson_printing():
    poisson = Poisson(seed=SEED, N=11)

    for s in ['N=11', 'rand_factor=0.01']:
        assert s in str(poisson)

    for s in ['N=11', 'xlim=(0, 31.195288877731507)', 'seed=31415927', 'lam=10.398429625910502', 'rand_factor=0.01']:
        assert s in repr(poisson)


def test_poisson_seeding():
    poisson1 = Poisson(seed=SEED)
    poisson2 = Poisson(seed=SEED)

    assert poisson1 != poisson2
    assert poisson1.lam == poisson2.lam

    assert all(np.array_equal(i, j) for i, j in zip(poisson1.data, poisson2.data))

def test_poisson_exceptions():
    with pytest.raises(GwydionError):
        Poisson(lam=2j)
    with pytest.raises(GwydionError):
        Poisson(lam='1234')

