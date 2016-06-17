import pytest
import numpy as np

from gwydion.stats import Binomial
from gwydion.exceptions import GwydionError


SEED = 31415927
TOLERANCE = 0.00001

def test_binom_creation():
    binom = Binomial()
    assert binom


def test_binom_non_random():
    binom = Binomial(rand=None, n=10, p=0.05, xlim=(0,10), N=7)
    x, y = binom.data

    for i, j in zip(x, [0, 1, 3, 5, 6, 8, 10]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, [5.98736939e-01, 3.15124705e-01, 1.04750594e-02, 6.09352488e-05, 2.67259863e-06, 1.58642578e-09, 9.76562500e-14]):
        assert abs(i - j) < TOLERANCE


def test_binom_random():
    x_test = [0, 1, 3, 5, 6, 8, 10]
    y_test = [0.00705519, 0.00548448, 0.00959058, 0.00911588, 0.02460644, 0.10608288, 0.23812268]

    binom = Binomial(seed=SEED, N=7, xlim=(0, 10))
    x, y = binom.data

    assert binom.n == 14
    assert binom.p == 0.7192932971412341

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_binom_variables():

    binom = Binomial(seed=SEED, N=7, xlim=(0, 10))

    assert binom.mean == 10.070106159977279
    assert binom.median == 10
    assert binom.mode == 10
    assert binom.variance == 2.8267462976049695
    assert binom.skewness == -0.26086267115548145


def test_binom_sampling():

    binom = Binomial(seed=SEED, N=7, xlim=(0, 20))

    single = binom.sample()
    assert single == 8

    sample = binom.sample(7)
    test = [9, 7, 9, 8, 10, 8, 8]
    for i, j in zip(sample, test):
        assert abs(i - j) < TOLERANCE


def test_binom_printing():
    binom = Binomial(seed=SEED, N=11)

    for s in ['N=11', 'rand=0.01']:
        assert s in str(binom)

    for s in ['N=11', 'xlim=(0, 14)', 'seed=31415927', 'n=14', 'p=0.7192932971412341', 'rand=0.01']:
        assert s in repr(binom)


def test_binom_seeding():
    binom1 = Binomial(seed=SEED)
    binom2 = Binomial(seed=SEED)

    assert binom1 != binom2
    assert binom1.n == binom2.n
    assert binom1.p == binom2.p

    assert all(np.array_equal(i, j) for i, j in zip(binom1.data, binom2.data))

def test_binom_exceptions():
    with pytest.raises(GwydionError):
        Binomial(n=2j)
    with pytest.raises(GwydionError):
        Binomial(p='1234')

