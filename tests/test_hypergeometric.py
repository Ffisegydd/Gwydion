import pytest
import numpy as np

from gwydion import Hypergeometric
from gwydion.exceptions import GwydionError


SEED = 31415927
TOLERANCE = 0.00001

def test_hyper_creation():
    hyper = Hypergeometric()
    assert hyper


def test_hyper_non_random():
    hyper = Hypergeometric(rand_factor=None, M=100, m=20, X=40, xlim=(0,20), N=7)
    x, y = hyper.data

    for i, j in zip(x, [0, 3, 6, 10, 13, 16, 20]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, [7.82084807e-06, 7.13781508e-03, 1.24220553e-01, 1.19236052e-01, 8.67063085e-03, 5.71825289e-05, 2.57184339e-10]):
        assert abs(i - j) < TOLERANCE


def test_hyper_random():
    x_test = [0, 3, 6, 10, 13, 16, 20]
    y_test = [0.00705517, 0.0054838, 0.01330298, 0.29433415, 0.01146449, 0.00080912, 0.00771055]

    hyper = Hypergeometric(seed=SEED, N=7, xlim=(0, 20))
    x, y = hyper.data

    assert hyper.M == 24
    assert hyper.m == 15
    assert hyper.X == 15

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_hyper_printing():
    hyper = Hypergeometric(seed=SEED, N=11)

    for s in ['N=11', 'rand_factor=0.01']:
        assert s in str(hyper)

    for s in ['N=11', 'xlim=(0, 15)', 'seed=31415927', 'M=24', 'X=15', 'm=15', 'rand_factor=0.01']:
        assert s in repr(hyper)


def test_hyper_seeding():
    hyper1 = Hypergeometric(seed=SEED)
    hyper2 = Hypergeometric(seed=SEED)

    assert hyper1 != hyper2
    assert hyper1.M == hyper2.M
    assert hyper1.m == hyper2.m
    assert hyper1.X == hyper2.X

    assert all(np.array_equal(i, j) for i, j in zip(hyper1.data, hyper2.data))

def test_hyper_exceptions():
    with pytest.raises(GwydionError):
        Hypergeometric(M=2j)
    with pytest.raises(GwydionError):
        Hypergeometric(m='1234')
    with pytest.raises(GwydionError):
        Hypergeometric(X='1234')

