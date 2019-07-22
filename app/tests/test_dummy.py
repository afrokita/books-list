import pytest


@pytest.fixture
def foo():
	bar = 42
	return bar

@pytest.mark.parametrize("num, output", [(42,42)])
def test_foo(num, output):
	assert num == output
