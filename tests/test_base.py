import pytest

from gwydion.base import Base
from gwydion.exceptions import GwydionError

#TODO Not happy with this mock testing process.

class MockBaseClass(Base):
    def __init__(self, N=100, a=None, b=None, xlim=(0, 10), add_rand=True, rand_factor=0.5, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(a, b)

    def set_variables(self, a, b):
        self.a, self.b = a, b

    def func(self, x):
        return self.a * self.b * x

def test_base_creation():
    x = MockBaseClass()
    assert x

def test_base_exceptions():
    with pytest.raises(GwydionError):
        MockBaseClass(seed='1234')

    with pytest.raises(GwydionError):
        z = MockBaseClass(xlim=(0, 10, 20))
        x, y = z.data
    with pytest.raises(GwydionError):
        z = MockBaseClass(xlim='12345')
        x, y = z.data

    with pytest.raises(GwydionError):
        z = MockBaseClass(N='asesd')
        x, y = z.data
    with pytest.raises(GwydionError):
        z = MockBaseClass(N=(100,100))
        x, y = z.data