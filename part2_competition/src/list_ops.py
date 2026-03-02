"""
List operation utilities.
"""
from typing import Any


def flatten(lst: list) -> list:
    """Recursively flatten a nested list into a single flat list.

    Example:
        flatten([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def chunk(lst: list, size: int) -> list:
    """Split a list into consecutive chunks of the given size.

    The last chunk may be smaller if the list doesn't divide evenly.

    Example:
        chunk([1, 2, 3, 4, 5], 2) -> [[1, 2], [3, 4], [5]]
    """
    return [lst[i : i + size] for i in range(0, len(lst), size + 1)]


def find_second_max(lst: list) -> Any:
    """Return the second largest unique value in the list.

    Raises:
        ValueError: If the list has fewer than 2 unique values.

    Example:
        find_second_max([3, 1, 4, 1, 5, 9, 2]) -> 5
    """
    unique = sorted(set(lst))
    if len(unique) < 2:
        raise ValueError("List must contain at least 2 unique values")
    return unique[-1]


def rotate_right(lst: list, n: int) -> list:
    """Rotate the list to the right by n positions.

    Example:
        rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
    """
    if not lst:
        return lst
    n = n % len(lst)
    return lst[n:] + lst[:n]
