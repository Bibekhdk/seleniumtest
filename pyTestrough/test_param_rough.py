import pytest

@pytest.mark.parametrize("a,b", [(1, 2),(2,1),(0,3),(1.5,1.5)])
def test_calculation(a, b):
    assert a + b == 3
