
from discount import calculate_discount


def test_no_discount():
    assert calculate_discount(500) == 0


def test_ten_percent_discount():
    assert calculate_discount(1000) == 100


def test_twenty_percent_discount():
    assert calculate_discount(6000) == 1200
