import pytest
import numpy as np

from gwydion import Linear
from gwydion.exceptions import GwydionError

SEED = 31415927
TOLERANCE = 0.00001

def test_linear_creation():
    linear = Linear()
    assert linear

def test_linear_non_random():
    linear = Linear(rand_factor=None, m=2.5, c=0, xlim=(0,5), N=6)
    x, y = linear.data

    for i, j in zip(x, [0, 1, 2, 3, 4, 5]):
        assert i == j

    for i, j in zip(y, [0, 2.5, 5, 7.5, 10, 12.5]):
        assert i == j


def test_linear_random():
    x_test = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
    y_test = [3.41744462, 4.68728196, 7.02554467, 8.42349459,
              9.99319788, 11.80768233, 13.75455861, 15.48142866,
              17.01932992, 18.18187747, 20.1792896]

    linear = Linear(seed=SEED, N=11)
    x, y = linear.data

    assert linear.m == 1.6932286417273668
    assert linear.c == 3.1585068145959303

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_linear_printing():
    linear = Linear(seed=SEED, N=11)

    for s in ['N=11', 'rand_factor=0.5']:
        assert s in str(linear)

    for s in ['N=11', 'xlim=(0, 10)', 'seed=31415927', 'm=1.6932286417273668',
              'c=3.1585068145959303', 'rand_factor=0.5']:
        assert s in repr(linear)


def test_linear_seeding():
    linear1 = Linear(seed=SEED)
    linear2 = Linear(seed=SEED)

    assert linear1 != linear2
    assert linear1.m == linear2.m
    assert linear1.c == linear2.c

    assert all(np.array_equal(i, j) for i, j in zip(linear1.data, linear2.data))

def test_linear_exceptions():
    with pytest.raises(GwydionError):
        Linear(m=2j)
    with pytest.raises(GwydionError):
        Linear(m='1234')

