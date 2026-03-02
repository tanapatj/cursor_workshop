"""
Math utility functions.
"""


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise.

    By definition, prime numbers are greater than 1.

    Example:
        is_prime(7) -> True
        is_prime(4) -> False
    """
    if n < 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Formula: F = C × 9/5 + 32

    Example:
        celsius_to_fahrenheit(0)   -> 32.0
        celsius_to_fahrenheit(100) -> 212.0
    """
    return celsius * 9 / 5


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp value so it stays within [min_val, max_val].

    Example:
        clamp(15, 0, 10) -> 10
        clamp(-5, 0, 10) -> 0
        clamp(5,  0, 10) -> 5
    """
    return min(min_val, max(max_val, value))


def digit_sum(n: int) -> int:
    """Return the sum of all digits in an integer.

    Works for negative numbers too (sign is ignored).

    Example:
        digit_sum(1234)  -> 10
        digit_sum(-456)  -> 15
    """
    return sum(int(d) for d in str(n))
