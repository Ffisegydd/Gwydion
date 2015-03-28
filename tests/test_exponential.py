import pytest
import numpy as np

from gwydion import Exponential
from gwydion.exceptions import GwydionError


SEED = 31415927
TOLERANCE = 0.00001

def test_exponential_creation():
    exp = Exponential()
    assert exp

def test_exponential_non_random():
    exp = Exponential(add_rand=False, k=-2.5, I=2, xlim=(0,5), N=6)
    x, y = exp.data

    for i, j in zip(x, [0, 1, 2, 3, 4, 5]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, [2.00000000e+00, 1.64169997e-01, 1.34758940e-02, 1.10616874e-03, 9.07998595e-05, 7.45330634e-06]):
        assert abs(i - j) < TOLERANCE


def test_exponential_random():
    x_test = [0., 1., 2., 3., 4., 5.]
    y_test = [0.97509472, 1.04837471, 1.36236306, 1.51993527, 1.7489186, 2.07025886]

    exp = Exponential(seed=SEED, N=6, xlim=(0,5))
    x, y = exp.data

    assert exp.k == 0.15792534072979653
    assert exp.I == 0.9233071604318417

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_exponential_printing():
    exp = Exponential(seed=SEED, N=11)

    for s in ['N=11', 'add_rand=True', 'rand_factor=0.1']:
        assert s in str(exp)

    for s in ['N=11', 'xlim=(-10, 10)', 'seed=31415927', 'I=0.9233071604318417',
              'base=2.718281828459045', 'k=0.15792534072979653', 'rand_factor=0.1', 'add_rand=True']:
        assert s in repr(exp)


def test_exponential_seeding():
    exp1 = Exponential(seed=SEED)
    exp2 = Exponential(seed=SEED)

    assert exp1 != exp2
    assert exp1.I == exp2.I
    assert exp1.k == exp2.k

    assert all(np.array_equal(i, j) for i, j in zip(exp1.data, exp2.data))

def test_exponential_exceptions():
    with pytest.raises(GwydionError):
        Exponential(k=2j)
    with pytest.raises(GwydionError):
        Exponential(I='1234')

