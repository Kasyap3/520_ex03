"""Baseline tests from Exercise 2"""
import pytest
from src.solutions import two_sum, is_palindrome

# Two Sum Tests
def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_negative():
    assert two_sum([-1, -2, -3, -4], -6) == [2, 3]

def test_two_sum_empty():
    assert two_sum([], 5) == []

def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 10) == []

def test_two_sum_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_large():
    assert two_sum([1000000, 2, 3, 4], 1000002) == [0, 1]

def test_two_sum_zero():
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]

def test_two_sum_first_last():
    assert two_sum([1, 5, 3, 7], 8) == [0, 3]

# Palindrome Tests
def test_palindrome_basic():
    assert is_palindrome("racecar") == True

def test_palindrome_mixed_case():
    assert is_palindrome("RaceCar") == True

def test_palindrome_with_spaces():
    assert is_palindrome("race a car") == False

def test_palindrome_empty():
    assert is_palindrome("") == True

def test_palindrome_single():
    assert is_palindrome("a") == True

def test_palindrome_special():
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_palindrome_numeric():
    assert is_palindrome("12321") == True

def test_palindrome_long():
    s = "a" * 100 + "b" + "a" * 100
    assert is_palindrome(s) == True

def test_palindrome_not():
    assert is_palindrome("hello world") == False

def test_palindrome_sentence():
    assert is_palindrome("Was it a car or a cat I saw?") == True
