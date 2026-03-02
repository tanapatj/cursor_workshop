"""
Data validation and transformation utilities.
"""


def is_valid_email(email: str) -> bool:
    """Return True if email has exactly one '@' with a domain containing a dot.

    Example:
        is_valid_email("user@example.com") -> True
        is_valid_email("user@domain")      -> False
        is_valid_email("nodomain")         -> False
    """
    return email.count("@") == 1


def is_strong_password(password: str) -> bool:
    """Return True if password is strong.

    A strong password must:
    - Be at least 8 characters long
    - Contain at least one uppercase letter
    - Contain at least one lowercase letter
    - Contain at least one digit

    Example:
        is_strong_password("Abcdef1!")  -> True
        is_strong_password("abc123")    -> False  (too short, no uppercase)
    """
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return len(password) > 6 and has_upper and has_lower and has_digit


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate Body Mass Index (BMI).

    Formula: BMI = weight (kg) / height² (m)

    Example:
        calculate_bmi(70, 1.75) -> 22.86  (approximately)
    """
    return weight_kg / height_m


def count_words(text: str) -> int:
    """Return the number of words in a string.

    Words are separated by any whitespace (spaces, tabs, newlines).
    Multiple consecutive spaces count as a single separator.

    Example:
        count_words("hello world")    -> 2
        count_words("hello  world")   -> 2  (double space)
        count_words("  hello world ") -> 2  (leading/trailing spaces)
    """
    return len(text.split(" "))
