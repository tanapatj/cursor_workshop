"""
Competition scoreboard for the Cursor Workshop Bug Hunt.

Run from the workspace root:
    python scripts/show_score.py
    make score
"""

import subprocess
import sys
import os
import re
from datetime import datetime

# ── ANSI colour helpers ────────────────────────────────────────────────────

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"


def color(text: str, *codes: str) -> str:
    return "".join(codes) + str(text) + RESET


# ── Constants ──────────────────────────────────────────────────────────────

MODULES = [
    ("string_utils", "String Utilities"),
    ("list_ops", "List Operations"),
    ("math_utils", "Math Utilities"),
    ("data_validator", "Data Validator"),
]

# ── Run pytest ─────────────────────────────────────────────────────────────


def run_tests() -> str:
    """Run competition tests and return combined stdout+stderr."""
    workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Run tests with verbose output so we can parse PASSED/FAILED per test
    test_result = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            "part2_competition/tests/",
            "-v", "--tb=no", "--no-header",
        ],
        capture_output=True,
        text=True,
        cwd=workspace,
    )

    # Run a quick coverage check separately (no per-test output needed)
    cov_result = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            "part2_competition/tests/",
            "--tb=no", "-q",
            "--cov=part2_competition/src",
            "--cov-report=term",
            "--no-header",
        ],
        capture_output=True,
        text=True,
        cwd=workspace,
    )

    return test_result.stdout + test_result.stderr + cov_result.stdout + cov_result.stderr


# ── Parse results ──────────────────────────────────────────────────────────


def parse_results(output: str) -> tuple[dict, dict, int]:
    """
    Returns:
        passed   – {module_key: count}
        failed   – {module_key: count}
        coverage – int percentage (0–100)
    """
    passed = {m: 0 for m, _ in MODULES}
    failed = {m: 0 for m, _ in MODULES}

    for line in output.splitlines():
        for module_key, _ in MODULES:
            if module_key in line:
                if " PASSED" in line:
                    passed[module_key] += 1
                elif " FAILED" in line:
                    failed[module_key] += 1

    coverage = 0
    cov_match = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", output)
    if cov_match:
        coverage = int(cov_match.group(1))

    return passed, failed, coverage


def totals(passed: dict, failed: dict) -> tuple[int, int]:
    """Return (total_passed, total_tests) across all modules."""
    tp = sum(passed.values())
    tt = sum(passed[m] + failed[m] for m, _ in MODULES)
    return tp, tt


# ── Display helpers ────────────────────────────────────────────────────────


def progress_bar(value: int, total: int, width: int = 20) -> str:
    if total == 0:
        filled = 0
    else:
        filled = round(value / total * width)
    empty = width - filled

    pct = value / total * 100 if total else 0

    if pct == 100:
        bar_color = GREEN
    elif pct >= 75:
        bar_color = CYAN
    elif pct >= 50:
        bar_color = YELLOW
    else:
        bar_color = RED

    bar = color("█" * filled, bar_color) + color("░" * empty, DIM)
    return f"[{bar}]"


def status_icon(passed: int, total: int) -> str:
    if passed == total:
        return color("✔ DONE", GREEN, BOLD)
    elif passed == 0:
        return color("✘ TODO", RED)
    else:
        return color("⟳ WIP ", YELLOW)


def module_score_line(label: str, passed: int, total: int) -> str:
    bar = progress_bar(passed, total, width=18)
    frac = f"{passed}/{total}"
    icon = status_icon(passed, total)
    pct = f"{passed/total*100:5.1f}%" if total else "  N/A "
    return f"  {label:<22}  {frac:>5}  {bar}  {pct}  {icon}"


def divider(char: str = "─", width: int = 72) -> str:
    return color(char * width, DIM)


# ── Main display ───────────────────────────────────────────────────────────


def display_scoreboard(passed: dict, failed: dict, coverage: int) -> None:
    total_passed, total_tests = totals(passed, failed)
    overall_pct = total_passed / total_tests * 100 if total_tests else 0

    now = datetime.now().strftime("%H:%M:%S")

    # ── Header ──
    print()
    print(color("╔" + "═" * 70 + "╗", CYAN))
    title = "  BUG HUNT COMPETITION — SCOREBOARD  "
    padding = (70 - len(title)) // 2
    print(color("║", CYAN) + " " * padding + color(title, BOLD, WHITE) + " " * (70 - len(title) - padding) + color("║", CYAN))
    print(color("╚" + "═" * 70 + "╝", CYAN))
    print()

    # ── Per-module results ──
    print(color("  MODULE                    SCORE  PROGRESS               PCT    STATUS", DIM))
    print(divider())

    for module_key, module_label in MODULES:
        p = passed[module_key]
        module_total = p + failed[module_key]
        print(module_score_line(module_label, p, module_total))

    print(divider())

    # ── Total score ──
    total_bar = progress_bar(total_passed, total_tests, width=18)
    total_frac = f"{total_passed}/{total_tests}"
    print(
        f"  {color('TOTAL SCORE', BOLD):<31}  {color(total_frac, BOLD):>5}  {total_bar}  "
        f"{color(f'{overall_pct:5.1f}%', BOLD)}"
    )

    # ── Coverage ──
    print(divider("─"))
    cov_bar = progress_bar(coverage, 100, width=18)
    cov_label = color("CODE COVERAGE", BOLD)
    cov_value = color(f"{coverage}%", CYAN if coverage >= 70 else YELLOW)
    print(f"  {cov_label:<31}  {color(str(coverage)+'%', BOLD):>5}  {cov_bar}  {cov_value}")

    # ── Motivational footer ──
    print()
    if total_passed == total_tests:
        print(color("  🏆  All tests passing! Outstanding work! 🏆", GREEN, BOLD))
    elif total_passed >= total_tests * 0.75:
        remaining = total_tests - total_passed
        print(color(f"  Almost there! Only {remaining} test(s) left — you've got this!", YELLOW))
    elif total_passed >= total_tests * 0.5:
        remaining = total_tests - total_passed
        print(color(f"  Halfway through! {remaining} test(s) remaining.", CYAN))
    else:
        print(color(f"  Keep going! Use Cursor to read the failing tests and fix the code.", DIM))

    print(color(f"  Last updated: {now}", DIM))
    print()


# ── Failing test hints ─────────────────────────────────────────────────────


def show_failing_hints(output: str) -> None:
    """Print a short list of which test names are still failing."""
    failing = []
    for line in output.splitlines():
        # Verbose line: "path::Class::test FAILED [ xx%]"
        if "::" in line and "FAILED" in line:
            match = re.search(r"::(\w+)::(\w+)\s+FAILED", line)
            if match:
                cls, fn = match.group(1), match.group(2)
                failing.append(f"  {color('✘', RED)} {cls}.{color(fn, YELLOW)}")

    if failing:
        print(color("  Still failing:", DIM))
        for hint in failing[:12]:
            print(hint)
        if len(failing) > 12:
            print(color(f"  ... and {len(failing)-12} more", DIM))
        print()


# ── Entry point ────────────────────────────────────────────────────────────


def main() -> None:
    print(color("  Running tests...", DIM), end="\r", flush=True)
    output = run_tests()
    passed, failed, coverage = parse_results(output)
    display_scoreboard(passed, failed, coverage)
    show_failing_hints(output)


if __name__ == "__main__":
    main()
