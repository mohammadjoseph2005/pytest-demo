import pytest
from calculator import Calculator


# ----------------------------------------------------------------------------------
# Fixture
# ----------------------------------------------------------------------------------
@pytest.fixture
def calc():
    """Return a fresh Calculator instance for each test."""
    return Calculator()


# ----------------------------------------------------------------------------------
# Parameterized arethmetic tests
# ----------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
        (-5, -5, -10),
    ],
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(5, 3, 2), (10, 20, -10), (-5, -5, 0), (10, 1, 9), (2.5, 1.5, 1.0)],
)
def test_subtact(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-2, 4, -8),
        (0, 100, 0),
        (2.5, 4, 10.0),
        (-3, -3, 9),
    ],
)
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),
        (5, 2, 2.5),
        (-10, 2, -5.0),
        (0, 5, 0.0),
        (7, 2, 3.5),
    ],
)
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected


@pytest.mark.parametrize(
    "base, exp, expected",
    [(2, 3, 8), (5, 0, 1), (3, 2, 9), (4, 0.5, 2.0), (10, -1, 0.1)],
)
def test_power(calc, base, exp, expected):
    assert calc.power(base, exp) == expected


# --------------------------------------------------------------------------------------------
# Exception tests
# --------------------------------------------------------------------------------------------
def test_devide_by_zero(calc):
    with pytest.raises(ValueError, match="Division by zero"):
        calc.divide(5, 0)


def test_add_invalid_type(calc):
    with pytest.raises(TypeError, match="Expected number"):
        calc.add("hello", 5)


def test_subtract_invalid_type(calc):
    with pytest.raises(TypeError):
        calc.subtract(10, [1, 2])


# --------------------------------------------------------------------------------------------------
# History tests
# --------------------------------------------------------------------------------------------------
def tst_history_recording(calc):
    calc.add(2, 3)
    calc.multiply(4, 5)
    hist = calc.history
    assert len(hist) == 2
    assert hist[0] == ("add", 2, 3, 5)
    assert hist[1] == ("multiply", 4, 5, 20)


def test_last_result(calc):
    assert calc.last_result() is None
    calc.subtract(10, 3)
    assert calc.last_result() == 7
    calc.power(2, 10)
    assert calc.last_result() == 1024


def test_clear_history(calc):
    calc.add(1, 1)
    calc.clear_history()
    assert len(calc.history) == 0
    assert calc.last_result() is None
