import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from part2_competition.src.list_ops import flatten, chunk, find_second_max, rotate_right


class TestFlatten:
    def test_already_flat(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_one_level_nested(self):
        assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]

    def test_deeply_nested(self):
        assert flatten([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

    def test_empty_list(self):
        assert flatten([]) == []


class TestChunk:
    def test_even_split(self):
        assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_uneven_split_last_chunk_smaller(self):
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_chunk_size_larger_than_list(self):
        assert chunk([1, 2], 5) == [[1, 2]]

    def test_single_element_chunks(self):
        assert chunk([1, 2, 3], 1) == [[1], [2], [3]]


class TestFindSecondMax:
    def test_basic_case(self):
        assert find_second_max([3, 1, 4, 1, 5, 9, 2]) == 5

    def test_two_elements(self):
        assert find_second_max([10, 20]) == 10

    def test_with_duplicates(self):
        assert find_second_max([5, 5, 5, 3]) == 3

    def test_raises_on_insufficient_unique_values(self):
        with pytest.raises(ValueError):
            find_second_max([7, 7, 7])


class TestRotateRight:
    def test_rotate_by_two(self):
        assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

    def test_rotate_by_one(self):
        assert rotate_right([1, 2, 3], 1) == [3, 1, 2]

    def test_rotate_full_length_returns_original(self):
        assert rotate_right([1, 2, 3], 3) == [1, 2, 3]

    def test_rotate_empty_list(self):
        assert rotate_right([], 3) == []
