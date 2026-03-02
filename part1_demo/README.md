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

### Step 3 — Ask Cursor to explain the failures

Select the failing test output, open Cursor Chat, and ask:

> *"These tests are failing. Can you look at the implementation in calculator.py and explain what's wrong?"*

### Step 4 — Fix the bugs

Use `Cmd+K` (inline edit) on the buggy line and ask Cursor to fix it.

After each fix, run `make test-part1` again to verify.

### Step 5 — All green ✅

Once all 3 bugs are fixed, all tests pass. Recap what Cursor helped with:
- Writing tests from scratch in seconds
- Reading test failures to pinpoint root causes
- Suggesting targeted fixes

---

## Bugs Reference (for facilitator only — don't share with audience!)

| Function | Bug | Fix |
|----------|-----|-----|
| `divide` | Uses integer division `//` | Change to `/` |
| `power` | Uses multiplication `*` instead of `**` | Change to `**` |
| `percentage` | Missing `* 100` | Add `* 100` |
