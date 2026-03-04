# Part 1 — Demo: Test-Driven Bug Discovery

## Facilitator Guide

This demo shows how Cursor makes it easy to write unit tests that expose hidden bugs — and then fix them.

**Duration:** 15–20 minutes  
**Format:** Live instructor demo (audience watches)

---

## The Code

`calculator.py` is a simple calculator module. It looks correct at first glance, but contains **3 hidden bugs** that only reveal themselves when tested with the right inputs.

Functions in the module:
- `add(a, b)` — addition
- `subtract(a, b)` — subtraction
- `multiply(a, b)` — multiplication
- `divide(a, b)` — division
- `power(a, b)` — exponentiation
- `percentage(value, total)` — percentage calculation

---

## Demo Script

### Step 1 — Explore the code with Cursor

Open `calculator.py`. Select all the code and open Cursor Chat (`Cmd+L`):

> *"Can you explain what each function does and write a comprehensive test suite for this calculator module?"*

Copy the suggested tests into `tests/test_calculator.py`.

### Step 2 — Run the tests

```bash
make test-part1
```

Some tests will **fail**. This is expected — the failures reveal the bugs!

### Step 3 — Ask Cursor to create test

Select the failing test output, open Cursor Chat, and ask:

> *"Please explain and write unit tests"*

