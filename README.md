# Cursor Workshop: AI-Powered Bug Hunting

A hands-on workshop teaching teams how to use [Cursor](https://cursor.sh) to write unit tests, identify bugs, and fix code faster with AI assistance.

---

## Workshop Overview

| Part | Type | Goal |
|------|------|------|
| **Part 1** | Demo (15–20 min) | Watch how Cursor helps write tests that expose hidden bugs |
| **Part 2** | Competition (30–45 min) | Race to fix the most bugs using Cursor |

---

## Prerequisites

- Python 3.8+
- [Cursor IDE](https://cursor.sh) installed
- Git

---

## Setup

```bash
# 1. Clone the repository
git clone <repo-url>
cd cursor-workshop

# 2. (Optional but recommended) Create a virtual environment
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify everything works
make check
```

---

## Part 1 — Demo: Writing Tests with Cursor

**Location:** `part1_demo/`

The instructor will live-demo how to use Cursor to:
1. Open `calculator.py` and ask Cursor to explain the code
2. Use Cursor to generate unit tests in `tests/test_calculator.py`
3. Run the tests and watch them **fail** — revealing hidden bugs
4. Ask Cursor to suggest fixes for each failing test
5. Run tests again until all pass ✅

```bash
# Run Part 1 tests
make test-part1

# Run with coverage
make coverage-part1
```

See `part1_demo/README.md` for detailed facilitator notes.

---

## Part 2 — Competition: Bug Hunt 🏆

**Location:** `part2_competition/`

- **16 hidden bugs** spread across 4 Python modules
- Tests are **already written** — your job is to fix the source code
- Use Cursor to understand failing tests, locate bugs, and fix them
- **Score = number of passing tests** (max 16)

```bash
# Show your current score (run this anytime!)
make score

# Run all competition tests
make test-part2

# Watch mode — auto-refresh score as you save files
make watch
```

### Modules & Bug Count

| Module | File | Bugs |
|--------|------|------|
| String Utilities | `src/string_utils.py` | 4 |
| List Operations | `src/list_ops.py` | 4 |
| Math Utilities | `src/math_utils.py` | 4 |
| Data Validator | `src/data_validator.py` | 4 |

### Tips for Using Cursor

- Open a failing test and press `Cmd+K` → ask *"Why is this test failing?"*
- Select the buggy function → `Cmd+L` → ask *"What is wrong with this function?"*
- Use `Cmd+I` inline edit to fix the bug directly
- Ask Cursor to explain edge cases you might be missing

See `part2_competition/README.md` for detailed competition rules.

---

## Quick Reference

```bash
make score        # Show competition scoreboard
make test-part1   # Run Part 1 tests
make test-part2   # Run Part 2 tests  
make coverage     # Show full coverage report
make watch        # Auto-refresh score on file changes
make clean        # Remove cache files
```
