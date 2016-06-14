import pytest
import numpy as np

from gwydion import Sine
from gwydion.exceptions import GwydionError


SEED = 31415927
TOLERANCE = 0.00001

def test_sine_creation():
    sine = Sine()
    assert sine


def test_sine_non_random():
    sine = Sine(rand_factor=None, f=0.7, I=2, p=0.0, xlim=(0, 5), N=6)
    x, y = sine.data

    for i, j in zip(x, [0, 1, 2, 3, 4, 5]):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, [0.00000000e+00, -1.90211303e+00, 1.17557050e+00, 1.17557050e+00, -1.90211303e+00, 1.71450552e-15]):
        assert abs(i - j) < TOLERANCE


def test_sine_random():
    x_test = [0., 1., 2., 3., 4., 5.]
    y_test = [0.08631519, 0.88651158, -0.71769869, -0.17114205, 0.93891486, -0.45470848]

    sine = Sine(seed=SEED, N=6, xlim=(0, 5))
    x, y = sine.data

    assert sine.I == 0.9233071604318417
    assert sine.f == 1.315850681459593
    assert sine.p == 0.1294689021043104

    for i, j in zip(x, x_test):
        assert abs(i - j) < TOLERANCE

    for i, j in zip(y, y_test):
        assert abs(i - j) < TOLERANCE


def test_sine_printing():
    sine = Sine(seed=SEED, N=11)

    for s in ['N=11', 'rand_factor=0.1']:
        assert s in str(sine)

    for s in ['N=11', 'xlim=(-10, 10)', 'seed=31415927', 'I=0.9233071604318417',
              'f=1.315850681459593', 'p=0.1294689021043104', 'rand_factor=0.1']:
        assert s in repr(sine)


def test_sine_seeding():
    sine1 = Sine(seed=SEED, xlim=(1,10))
    sine2 = Sine(seed=SEED, xlim=(1,10))

    assert sine1 != sine2
    assert sine1.I == sine2.I
    assert sine1.f == sine2.f
    assert sine1.p == sine2.p

    assert all(np.array_equal(i, j) for i, j in zip(sine1.data, sine2.data))

def test_sine_exceptions():
    with pytest.raises(GwydionError):
        Sine(f=2j)
    with pytest.raises(GwydionError):
        Sine(I='1234')

