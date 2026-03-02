import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from part2_competition.src.string_utils import (
    reverse_string,
    count_vowels,
    truncate,
    snake_to_camel,
)


class TestReverseString:
    def test_reverse_simple_word(self):
        assert reverse_string("hello") == "olleh"

    def test_reverse_sentence_reverses_characters_not_words(self):
        assert reverse_string("hello world") == "dlrow olleh"

    def test_reverse_empty_string(self):
        assert reverse_string("") == ""

    def test_reverse_single_character(self):
        assert reverse_string("a") == "a"


class TestCountVowels:
    def test_count_lowercase_vowels(self):
        assert count_vowels("hello") == 2

    def test_count_uppercase_vowels(self):
        assert count_vowels("HELLO") == 2

    def test_count_mixed_case_vowels(self):
        assert count_vowels("Hello World") == 3

    def test_count_no_vowels(self):
        assert count_vowels("rhythm") == 0


class TestTruncate:
    def test_no_truncation_when_short_enough(self):
        assert truncate("hello", 10) == "hello"

    def test_total_length_never_exceeds_max_len(self):
        result = truncate("Hello, World!", 8)
        assert len(result) <= 8

    def test_truncated_string_ends_with_suffix(self):
        result = truncate("Hello, World!", 8)
        assert result.endswith("...")

    def test_custom_suffix(self):
        result = truncate("Hello, World!", 7, suffix="…")
        assert len(result) <= 7
        assert result.endswith("…")


class TestSnakeToCamel:
    def test_basic_conversion(self):
        assert snake_to_camel("hello_world") == "helloWorld"

    def test_first_word_stays_lowercase(self):
        assert snake_to_camel("hello_world_foo") == "helloWorldFoo"

    def test_single_word_unchanged(self):
        assert snake_to_camel("hello") == "hello"

    def test_multiple_words(self):
        assert snake_to_camel("get_user_by_id") == "getUserById"
