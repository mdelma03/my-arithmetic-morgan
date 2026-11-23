import pytest
from my_arithmetic_morgan import pgcd


def test_pgcd_cas_classiques():
    assert pgcd(48, 18) == 6
    assert pgcd(18, 48) == 6
    assert pgcd(101, 103) == 1  # Nombres premiers entre eux


def test_pgcd_avec_zero():
    assert pgcd(0, 5) == 5
    assert pgcd(7, 0) == 7


def test_pgcd_nombres_negatifs():
    assert pgcd(-48, 18) == 6
    assert pgcd(48, -18) == 6
    assert pgcd(-48, -18) == 6


def test_pgcd_double_zero_erreur():
    with pytest.raises(ValueError):
        pgcd(0, 0)