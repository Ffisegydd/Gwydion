import pytest
import numpy as np

from gwydion import Linear


def test_linear_creation():
    linear = Linear()
    assert linear


def test_linear_non_random():
    linear = Linear(add_rand=False, m=2.5, c=0, xlim=(0,5), N=6)
    x, y = linear.data

    for i, j in zip(x, [0, 1, 2, 3, 4, 5]):
        assert i == j

    for i, j in zip(y, [0, 2.5, 5, 7.5, 10, 12.5]):
        assert i == j


def test_linear_seeding():

    seed = 123456789

    linear1 = Linear(seed=seed)
    linear2 = Linear(seed=seed)

    assert linear1 != linear2
    assert linear1.m == linear2.m
    assert linear1.c == linear2.c

    assert all(np.array_equal(i, j) for i, j in zip(linear1.data, linear2.data))




