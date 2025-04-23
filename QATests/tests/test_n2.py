import pytest


def func(x):
    if x < 0:
        raise ValueError("x must be non-negative")
    return x**2

@pytest.mark.parametrize(
    "x",
    [
        -1,
        1,
        0,
        20
    ]
)
def test_func(x):
    with pytest.raises((ValueError, ZeroDivisionError)) as excinfo:
        func(x)
    # assert str(excinfo.value) == "x must be non-negative"
