"""Exercise 3 Solutions"""
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of two numbers that add up to target."""
    if not nums:
        return []
    
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []


def is_palindrome(s: str) -> bool:
    """Check if string is palindrome (alphanumeric, case-insensitive)."""
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
