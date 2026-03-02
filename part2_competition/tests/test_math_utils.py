import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from part2_competition.src.math_utils import (
    is_prime,
    celsius_to_fahrenheit,
    clamp,
    digit_sum,
)


class TestIsPrime:
    def test_one_is_not_prime(self):
        assert is_prime(1) is False

    def test_zero_is_not_prime(self):
        assert is_prime(0) is False

    def test_two_is_prime(self):
        assert is_prime(2) is True

    def test_known_primes(self):
        for p in [3, 5, 7, 11, 13, 97]:
            assert is_prime(p) is True, f"{p} should be prime"

    def test_known_composites(self):
        for c in [4, 6, 9, 15, 100]:
            assert is_prime(c) is False, f"{c} should not be prime"


class TestCelsiusToFahrenheit:
    def test_freezing_point(self):
        assert celsius_to_fahrenheit(0) == 32.0

    def test_boiling_point(self):
        assert celsius_to_fahrenheit(100) == 212.0

    def test_body_temperature(self):
        assert abs(celsius_to_fahrenheit(37) - 98.6) < 0.1

    def test_negative_celsius(self):
        assert celsius_to_fahrenheit(-40) == -40.0


class TestClamp:
    def test_value_above_max_returns_max(self):
        assert clamp(15, 0, 10) == 10

    def test_value_below_min_returns_min(self):
        assert clamp(-5, 0, 10) == 0

    def test_value_within_range_unchanged(self):
        assert clamp(5, 0, 10) == 5

    def test_value_at_boundary(self):
        assert clamp(0, 0, 10) == 0
        assert clamp(10, 0, 10) == 10


class TestDigitSum:
    def test_positive_number(self):
        assert digit_sum(1234) == 10

    def test_single_digit(self):
        assert digit_sum(7) == 7

    def test_negative_number(self):
        assert digit_sum(-456) == 15

    def test_zero(self):
        assert digit_sum(0) == 0
