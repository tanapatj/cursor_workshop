import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from part2_competition.src.data_validator import (
    is_valid_email,
    is_strong_password,
    calculate_bmi,
    count_words,
)


class TestIsValidEmail:
    def test_valid_email(self):
        assert is_valid_email("user@example.com") is True

    def test_missing_dot_in_domain_is_invalid(self):
        assert is_valid_email("user@domain") is False

    def test_missing_at_sign_is_invalid(self):
        assert is_valid_email("userdomain.com") is False

    def test_multiple_at_signs_is_invalid(self):
        assert is_valid_email("a@@b.com") is False


class TestIsStrongPassword:
    def test_strong_password(self):
        assert is_strong_password("Abcdef1!") is True

    def test_exactly_8_chars_is_strong(self):
        assert is_strong_password("Abcdef1x") is True

    def test_7_chars_is_not_strong(self):
        assert is_strong_password("Abcde1x") is False

    def test_no_uppercase_is_not_strong(self):
        assert is_strong_password("abcdef12") is False

    def test_no_digit_is_not_strong(self):
        assert is_strong_password("Abcdefgh") is False


class TestCalculateBmi:
    def test_normal_bmi(self):
        result = calculate_bmi(70, 1.75)
        assert abs(result - 22.86) < 0.1

    def test_bmi_formula_uses_height_squared(self):
        result = calculate_bmi(80, 2.0)
        assert result == 20.0

    def test_bmi_overweight(self):
        result = calculate_bmi(90, 1.70)
        assert abs(result - 31.14) < 0.1

    def test_bmi_underweight(self):
        result = calculate_bmi(45, 1.70)
        assert result < 18.5


class TestCountWords:
    def test_simple_sentence(self):
        assert count_words("hello world") == 2

    def test_double_space_still_two_words(self):
        assert count_words("hello  world") == 2

    def test_leading_and_trailing_spaces(self):
        assert count_words("  hello world  ") == 2

    def test_single_word(self):
        assert count_words("hello") == 1
