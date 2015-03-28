import pytest
import numpy as np

from gwydion import Logarithm
from gwydion.exceptions import GwydionError


SEED = 31415927
TOLERANCE = 0.00001

def test_logarithm_creation():
    log = Logarithm()
    assert log

def test_logarithm_non_random():
    log = Logarithm(add_rand=False, k=2.5, I=2, xlim=(1,6), N=6)
    x, y = log.data

    for i, j in zip(x, [1, 2, 3, 4, 5, 6]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, [1.83258146, 3.21887582, 4.02980604, 4.60517019, 5.05145729, 5.4161004]):
        assert abs(i - j) < TOLERANCE


def test_logarithm_random():
    x_test = [1., 2., 3., 4., 5., 6.]
    y_test = [-1.6522985, -1.096989, -0.59361335, -0.38705018, -0.20572521, -0.01313525]

    log = Logarithm(seed=SEED, N=6, xlim=(1,6))
    x, y = log.data

    assert log.k == 0.15792534072979653
    assert log.I == 0.9233071604318417

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_logarithm_printing():
    log = Logarithm(seed=SEED, N=11)

    for s in ['N=11', 'add_rand=True', 'rand_factor=0.1']:
        assert s in str(log)

    for s in ['N=11', 'xlim=(-10, 10)', 'seed=31415927', 'I=0.9233071604318417',
              'base=2.718281828459045', 'k=0.15792534072979653', 'rand_factor=0.1', 'add_rand=True']:
        assert s in repr(log)


def test_logarithm_seeding():
    log1 = Logarithm(seed=SEED, xlim=(1,10))
    log2 = Logarithm(seed=SEED, xlim=(1,10))

    assert log1 != log2
    assert log1.I == log2.I
    assert log1.k == log2.k

    print(log1.data, log2.data)

    assert all(np.array_equal(i, j) for i, j in zip(log1.data, log2.data))

def test_logarithm_exceptions():
    with pytest.raises(GwydionError):
        Logarithm(k=2j)
    with pytest.raises(GwydionError):
        Logarithm(I='1234')

