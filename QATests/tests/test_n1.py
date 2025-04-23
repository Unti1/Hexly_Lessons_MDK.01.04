import pytest

@pytest.mark.parametrize(
    "param1, param2",
    [
        (1, 4), 
        (2, 3), 
        (3, 3),
        (3, 2),
        (3, 5),
        ]

)
def test_parametrize(param1, param2):
    assert param1 + param2 == 5