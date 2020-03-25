import pytest

@pytest.mark.parametrize("a,b", [(1,2)])
def test_sum(a,b):
        assert (a+b) == 3


