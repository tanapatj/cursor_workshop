"""
String utility functions.
"""


def reverse_string(s: str) -> str:
    """Return the string with its characters in reverse order.

    Example:
        reverse_string("hello world") -> "dlrow olleh"
    """
    words = s.split()
    return " ".join(reversed(words))


def count_vowels(s: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the string.

    Vowel counting is case-insensitive.

    Example:
        count_vowels("Hello World") -> 3
    """
    return sum(1 for c in s if c in "aeiou")


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    """Truncate a string to max_len characters, appending suffix if truncated.

    The total length of the returned string will never exceed max_len.

    Example:
        truncate("Hello, World!", 8) -> "Hello..."
    """
    if len(s) <= max_len:
        return s
    return s[:max_len] + suffix


def snake_to_camel(s: str) -> str:
    """Convert a snake_case string to camelCase.

    Example:
        snake_to_camel("hello_world_foo") -> "helloWorldFoo"
    """
    components = s.split("_")
    return "".join(x.title() for x in components)
