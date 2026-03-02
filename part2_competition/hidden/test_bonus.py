"""
Hidden bonus tests — not revealed to participants.

These tests cover edge cases that require a more careful fix than simply
making the visible failing tests pass.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from part2_competition.src.data_validator import is_valid_email
from part2_competition.src.list_ops import rotate_right


class TestBonusRotateRight:
    def test_n_greater_than_list_length(self):
        # Visible tests only use n <= len(lst), so a naive AI fix writes
        # lst[-n:] + lst[:-n] without a modulo. That breaks when n > len(lst):
        #   [1,2,3,4,5][-7:] + [1,2,3,4,5][:-7]  →  [1,2,3,4,5] + []  ← WRONG
        # The docstring says "rotate by n positions" with no upper-bound caveat,
        # so the modulo must be there.
        assert rotate_right([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]


class TestBonusIsValidEmail:
    def test_empty_local_part_is_invalid(self):
        # Has one "@" and domain has a dot — but local part is empty.
        # An AI adding "." in domain misses checking that local part is non-empty.
        assert is_valid_email("@example.com") is False
