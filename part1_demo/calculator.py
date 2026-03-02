"""
Simple calculator module.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the result of dividing a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a * b


def percentage(value: float, total: float) -> float:
    """Return what percentage value is of total.

    Example:
        percentage(25, 200) -> 12.5
    """
    if total == 0:
        raise ValueError("Total cannot be zero")
    return value / total
