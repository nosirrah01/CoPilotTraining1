from typing import Iterable, Sequence


def calculate_average(numbers: Sequence[float]) -> float:
    """Return the average of a sequence of numbers. Returns 0 for empty input."""
    count = len(numbers)
    if count == 0:
        return 0
    return sum(numbers) / count

def binary_search(items: Sequence[float], target: float) -> int:
    """Perform binary search on a sorted sequence. Return index or -1 if not found."""
    left, right = 0, len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def reverse_string(s: str) -> str:
    """Return the reversed string."""
    return s[::-1]

def test_calculate_average_empty_returns_zero():
    assert calculate_average([]) == 0


def test_calculate_average_with_values():
    assert calculate_average([2, 4, 6, 8]) == 5


def test_binary_search_finds_existing_item():
    assert binary_search([1, 3, 5, 7, 9], 7) == 3


def test_binary_search_returns_negative_one_for_missing_item():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_reverse_string_with_regular_text():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_with_empty_text():
    assert reverse_string("") == ""


def test_reverse_string_with_palindrome():
    assert reverse_string("level") == "level"