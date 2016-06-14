import pytest
import numpy as np

from gwydion import Normal
from gwydion.exceptions import GwydionError


SEED = 31415927
TOLERANCE = 0.00001

def test_normal_creation():
    normal = Normal()
    assert normal


def test_normal_non_random():
    normal = Normal(rand_factor=None, mu=0.0, sigma=2, xlim=(-3,3), N=7)
    x, y = normal.data

    for i, j in zip(x, [-3, -2, -1, 0, 1, 2, 3]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, [0.0647588, 0.12098536, 0.17603266, 0.19947114, 0.17603266, 0.12098536, 0.0647588]):
        assert abs(i - j) < TOLERANCE


def test_normal_random():
    x_test = [-3., -2., -1., 0., 1., 2., 3.]
    y_test = [0.01035751, -0.00656358, 0.09470932, 0.96825844, 0.03250045, 0.0073236, 0.0174672]

    normal = Normal(seed=SEED, N=7, xlim=(-3, 3))
    x, y = normal.data

    assert normal.mu == -0.07669283956815831
    assert normal.sigma == 0.4079253407297965

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_normal_printing():
    normal = Normal(seed=SEED, N=11)

    for s in ['N=11', 'rand_factor=0.02']:
        assert s in str(normal)

    for s in ['N=11', 'xlim=(-2.1163195432171413, 1.9629338640808245)', 'seed=31415927', 'mu=-0.07669283956815831',
              'sigma=0.4079253407297965', 'rand_factor=0.02']:
        assert s in repr(normal)


def test_normal_seeding():
    normal1 = Normal(seed=SEED)
    normal2 = Normal(seed=SEED)

    assert normal1 != normal2
    assert normal1.mu == normal2.mu
    assert normal1.sigma == normal2.sigma

    assert all(np.array_equal(i, j) for i, j in zip(normal1.data, normal2.data))

def test_normal_exceptions():
    with pytest.raises(GwydionError):
        Normal(mu=2j)
    with pytest.raises(GwydionError):
        Normal(sigma='1234')

