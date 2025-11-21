"""Spec-guided tests from Part 2"""
import pytest
from src.solutions import two_sum, is_palindrome

# ========== TWO SUM SPEC-GUIDED TESTS ==========

def test_spec_guided_two_sum_type_check():
    """Validates Spec 1: Result must be a list"""
    result = two_sum([2, 7, 11, 15], 9)
    assert isinstance(result, list)
    
    result = two_sum([], 5)
    assert isinstance(result, list)


def test_spec_guided_two_sum_length():
    """Validates Spec 2: Result length is 0 or 2"""
    result = two_sum([2, 7, 11, 15], 9)
    assert len(result) == 2
    
    result = two_sum([1, 2, 3], 10)
    assert len(result) == 0


def test_spec_guided_two_sum_valid_indices():
    """Validates Spec 3: Indices must be valid array positions"""
    nums = [2, 7, 11, 15]
    result = two_sum(nums, 9)
    assert len(result) == 2
    assert 0 <= result[0] < len(nums)
    assert 0 <= result[1] < len(nums)


def test_spec_guided_two_sum_different_indices():
    """Validates Spec 4: Two indices must be different"""
    result = two_sum([3, 3], 6)
    assert len(result) == 2
    assert result[0] != result[1]


def test_spec_guided_two_sum_correct_sum():
    """Validates Spec 5: Sum equals target"""
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    assert len(result) == 2
    assert nums[result[0]] + nums[result[1]] == target


def test_spec_guided_two_sum_edge_empty():
    """Validates all specs with empty array"""
    result = two_sum([], 5)
    assert isinstance(result, list)  # Spec 1
    assert len(result) == 0  # Spec 2


def test_spec_guided_two_sum_edge_single():
    """Validates specs with single element (no solution)"""
    result = two_sum([5], 10)
    assert isinstance(result, list)  # Spec 1
    assert len(result) == 0  # Spec 2


def test_spec_guided_two_sum_negative_target():
    """Validates specs with negative numbers"""
    nums = [-5, -2, -3, -1]
    target = -7
    result = two_sum(nums, target)
    assert isinstance(result, list)  # Spec 1
    assert len(result) == 2  # Spec 2
    assert result[0] != result[1]  # Spec 4
    assert nums[result[0]] + nums[result[1]] == target  # Spec 5


# ========== PALINDROME SPEC-GUIDED TESTS ==========

def test_spec_guided_palindrome_type_check():
    """Validates Spec 1: Result must be boolean"""
    result = is_palindrome("racecar")
    assert isinstance(result, bool)
    
    result = is_palindrome("hello")
    assert isinstance(result, bool)


def test_spec_guided_palindrome_empty_string():
    """Validates Spec 2: Empty string is palindrome"""
    result = is_palindrome("")
    assert result == True


def test_spec_guided_palindrome_single_char():
    """Validates Spec 3: Single character is palindrome"""
    result = is_palindrome("a")
    assert result == True
    
    result = is_palindrome("Z")
    assert result == True
    
    result = is_palindrome("5")
    assert result == True


def test_spec_guided_palindrome_case_insensitive():
    """Validates Spec 4: Case insensitivity"""
    test_string = "RaceCar"
    filtered = ''.join(c.lower() for c in test_string if c.isalnum())
    expected = (filtered == filtered[::-1])
    result = is_palindrome(test_string)
    assert result == expected


def test_spec_guided_palindrome_ignore_special():
    """Validates Spec 5: Non-alphanumeric ignored"""
    test_string = "A man, a plan, a canal: Panama"
    filtered = ''.join(c.lower() for c in test_string if c.isalnum())
    expected = (filtered == filtered[::-1])
    result = is_palindrome(test_string)
    assert result == expected


def test_spec_guided_palindrome_numbers_only():
    """Validates specs with numeric palindrome"""
    result = is_palindrome("12321")
    filtered = "12321"
    expected = (filtered == filtered[::-1])
    assert result == expected


def test_spec_guided_palindrome_mixed_special_chars():
    """Validates Spec 5 with heavy special characters"""
    test_string = "!@#$%A^&*()B___B{}[]A"
    filtered = ''.join(c.lower() for c in test_string if c.isalnum())
    expected = (filtered == filtered[::-1])
    result = is_palindrome(test_string)
    assert result == expected


def test_spec_guided_palindrome_not_palindrome():
    """Validates specs when string is NOT a palindrome"""
    test_string = "hello world"
    filtered = ''.join(c.lower() for c in test_string if c.isalnum())
    expected = (filtered == filtered[::-1])
    result = is_palindrome(test_string)
    assert result == expected
    assert result == False
