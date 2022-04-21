from pytest import approx

from functions import square_root, circle_area


def test_math_functions():
    assert square_root(9) == 3
    assert circle_area(3) == approx(28.3, 0.1)
