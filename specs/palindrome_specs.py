"""Palindrome Specifications - Part 1"""

# ========== LLM GENERATED SPECS (Original) ==========

# Specification 1: Result must be a boolean value
# assert isinstance(res, bool)

# Specification 2: Empty string should return True
# assert s == "" implies res == True

# Specification 3: Single character strings are always palindromes
# filtered = ''.join(c.lower() for c in s if c.isalnum())
# assert len(filtered) == 1 implies res == True

# Specification 4: The result should be case-insensitive
# import random
# assert is_palindrome(s) == is_palindrome(s.upper()) == is_palindrome(s.lower())

# Specification 5: Non-alphanumeric characters should be ignored
# filtered = ''.join(c.lower() for c in s if c.isalnum())
# assert res == (filtered == filtered[::-1])

# ========== EVALUATION ==========

# Spec 1: ✅ CORRECT - Proper type check
# Spec 2: ✅ CORRECT - Correct boundary condition
# Spec 3: ✅ CORRECT - Valid single character check
# Spec 4: ❌ INCORRECT - Calls is_palindrome() in assertion (self-reference) AND imports random (side effect)
# Spec 5: ✅ CORRECT - Properly checks palindrome property without calling function

TOTAL_GENERATED = 5
CORRECT = 4
INCORRECT = 1
ACCURACY = 0.8  # 80%

# ========== ISSUES WITH INCORRECT SPECS ==========

# Spec 4 Issues:
# - Calls is_palindrome() multiple times (self-reference violation)
# - Imports random module unnecessarily (not used but shows intent for side effects)
# - Should describe the property without calling the function

# ========== CORRECTED SPECIFICATIONS ==========

def spec1(s, res):
    """Result must be a boolean"""
    return isinstance(res, bool)

def spec2(s, res):
    """Empty string is a palindrome"""
    if s == "":
        return res == True
    return True

def spec3(s, res):
    """Single alphanumeric character is palindrome"""
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    if len(filtered) == 1:
        return res == True
    return True

def spec4_corrected(s, res):
    """Result is based on alphanumeric content only (case-insensitive)"""
    # CORRECTED: Check the filtered string property directly
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    expected = (filtered == filtered[::-1])
    return res == expected

def spec5(s, res):
    """Non-alphanumeric characters ignored"""
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    expected = (filtered == filtered[::-1])
    return res == expected

# ========== VERIFICATION ==========

if __name__ == "__main__":
    from src.solutions import is_palindrome
    
    # Test specifications
    test_cases = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "hello",
        "",
        "a",
        "Was it a car or a cat I saw?"
    ]
    
    print("Palindrome Specification Verification:\n")
    for s in test_cases:
        res = is_palindrome(s)
        print(f"Input: '{s}'")
        print(f"Output: {res}")
        
        assert spec1(s, res), "Spec 1 failed"
        assert spec2(s, res), "Spec 2 failed"
        assert spec3(s, res), "Spec 3 failed"
        assert spec4_corrected(s, res), "Spec 4 failed"
        assert spec5(s, res), "Spec 5 failed"
        
        print("✅ All specs passed\n")
    
    print(f"Accuracy: {CORRECT}/{TOTAL_GENERATED} = {ACCURACY*100}%")
