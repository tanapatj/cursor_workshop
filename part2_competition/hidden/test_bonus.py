"""
Hidden bonus tests — not revealed to participants.

These tests cover edge cases that require a more careful fix than simply
making the visible failing tests pass.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from part2_competition.src.data_validator import count_words, is_valid_email


class TestBonusCountWords:
    def test_empty_string_is_zero_words(self):
        # split(" ") returns [""] for empty string (len 1), split() returns [] (len 0)
        assert count_words("") == 0


class TestBonusIsValidEmail:
    def test_empty_local_part_is_invalid(self):
        # Has one "@" and domain has a dot — but local part is empty
        assert is_valid_email("@example.com") is False
