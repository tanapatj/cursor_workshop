"""
Unit tests for calculator.py

--- WORKSHOP DEMO FILE ---
This file is intentionally sparse.

During the demo, the instructor will use Cursor to generate tests here.
Suggested prompt to try in Cursor Chat (Cmd+L):

  "Look at part1_demo/calculator.py and write a comprehensive test suite
   that covers normal cases, edge cases, and potential error conditions."

Then run:  make test-part1
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from calculator import add, subtract, multiply, divide, power, percentage


# ── Example test (already written to get you started) ──────────────────────

def test_add_positive_numbers():
    assert add(2, 3) == 5


# ── Write the rest of the tests below with Cursor's help ───────────────────
#
# Things to test:
#   - divide(10, 2), divide(7, 2), divide(1, 3)   <-- try non-integer results!
#   - power(2, 3), power(3, 0), power(2, 10)
#   - percentage(25, 200), percentage(50, 50), percentage(1, 3)
#   - Edge cases: divide by zero, percentage with zero total
