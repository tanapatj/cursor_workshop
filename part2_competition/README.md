# Part 2 — Competition: Bug Hunt 🏆

## Rules

1. **You may only edit files inside `part2_competition/src/`** — do not modify the test files
2. There are **16 hidden bugs** — 4 in each source module
3. **Score = number of passing tests** (max 16)
4. Check your score at any time with `make score`
5. Highest score wins! Tiebreaker: earliest time all bugs are fixed

---

## How to Play

### 1. See your current score

```bash
make score
```

This shows a live scoreboard: which modules are fixed, how many tests pass, and your code coverage.

### 2. Run the full test suite

```bash
make test-part2
```

### 3. Use Cursor to find and fix bugs

**Recommended Cursor workflow:**

```
# Open a failing test and ask Cursor:
Cmd+L → "This test is failing. Look at the implementation in src/ and explain why."

# Select the buggy function and ask:
Cmd+K → "Fix this function so it matches the docstring and passes the tests."

# After fixing, check your score:
make score
```

### 4. Repeat until all 16 tests pass!

---

## Files

```
part2_competition/
├── src/                       ← Edit these files to fix bugs
│   ├── string_utils.py        (4 bugs)
│   ├── list_ops.py            (4 bugs)
│   ├── math_utils.py          (4 bugs)
│   └── data_validator.py      (4 bugs)
└── tests/                     ← DO NOT EDIT
    ├── test_string_utils.py
    ├── test_list_ops.py
    ├── test_math_utils.py
    └── test_data_validator.py
```

---

## Hints (only if you're stuck)

<details>
<summary>string_utils.py — hints</summary>

- One function reverses the wrong thing
- One function has a case-sensitivity issue
- One function doesn't account for its own suffix length
- One function capitalises too many words

</details>

<details>
<summary>list_ops.py — hints</summary>

- One function only goes one level deep when it should go all the way
- One function has an off-by-one in its range step
- One function returns the wrong ranked element
- One function rotates in the wrong direction

</details>

<details>
<summary>math_utils.py — hints</summary>

- One function has a wrong boundary condition for a well-known definition
- One function is missing a constant in a conversion formula
- One function has its min/max logic inverted
- One function crashes on a certain category of input

</details>

<details>
<summary>data_validator.py — hints</summary>

- One function validates one condition but forgets another
- One function uses `>` when it should use `>=`
- One function is missing an exponent in its formula
- One function splits on a single character instead of any whitespace

</details>
