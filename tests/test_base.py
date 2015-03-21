import pytest
import numpy as np

from gwydion.base import Base
from gwydion.exceptions import GwydionError

class MockBaseClass(Base):
    def __init__(self, N=100, a=None, b=None, c=None, xlim=(0, 10), add_rand=True, rand_factor=0.5, seed=None):
        super().__init__(N=N,
                         xlim=xlim,
                         add_rand=add_rand,
                         rand_factor=rand_factor,
                         seed=seed)

        self.set_variables(a, b, c)

    def set_variables(self, a, b, c):
        pass

    def func(self, x):
        pass

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