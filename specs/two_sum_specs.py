"""Two Sum Specifications - Part 1"""

# ========== LLM GENERATED SPECS (Original) ==========

# Specification 1: Result must be a list
# assert isinstance(res, list)

# Specification 2: Result length must be either 0 (no solution) or 2 (one solution)
# assert len(res) == 0 or len(res) == 2

# Specification 3: If solution exists, indices must be valid and within array bounds
# assert len(res) == 0 or (0 <= res[0] < len(nums) and 0 <= res[1] < len(nums))

# Specification 4: If solution exists, the two indices must be different
# assert len(res) == 0 or res[0] != res[1]

# Specification 5: If solution exists, verify the sum equals target
# result = two_sum(nums, target)
# assert len(result) == 0 or nums[result[0]] + nums[result[1]] == target

# ========== EVALUATION ==========

# Spec 1: ✅ CORRECT - Properly checks return type
# Spec 2: ✅ CORRECT - Valid length constraint  
# Spec 3: ✅ CORRECT - Checks valid array indices
# Spec 4: ✅ CORRECT - Ensures no duplicate index usage
# Spec 5: ❌ INCORRECT - Calls two_sum() inside assertion (self-reference violation)

TOTAL_GENERATED = 5
CORRECT = 4
INCORRECT = 1
ACCURACY = 0.8  # 80%

# ========== ISSUES WITH INCORRECT SPECS ==========

# Spec 5 Issue:
# - Calls two_sum(nums, target) inside the assertion
# - This is self-reference - specification should NOT call the function being specified
# - Specifications should describe the relationship between inputs (nums, target) and output (res)

# ========== CORRECTED SPECIFICATIONS ==========

def spec1(nums, target, res):
    """Result must be a list"""
    return isinstance(res, list)

def spec2(nums, target, res):
    """Result length must be 0 or 2"""
    return len(res) == 0 or len(res) == 2

def spec3(nums, target, res):
    """If solution exists, indices must be valid"""
    return len(res) == 0 or (0 <= res[0] < len(nums) and 0 <= res[1] < len(nums))

def spec4(nums, target, res):
    """Two indices must be different"""
    return len(res) == 0 or res[0] != res[1]

def spec5_corrected(nums, target, res):
    """If solution exists, the sum must equal target"""
    # CORRECTED: Use res directly instead of calling two_sum()
    return len(res) == 0 or nums[res[0]] + nums[res[1]] == target

# ========== VERIFICATION ==========

if __name__ == "__main__":
    from src.solutions import two_sum
    
    # Test specifications
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 3], 6, [0, 1]),
        ([], 5, []),
        ([1, 2, 3], 10, []),
    ]
    
    print("Two Sum Specification Verification:\n")
    for nums, target, expected in test_cases:
        res = two_sum(nums, target)
        print(f"Input: nums={nums}, target={target}")
        print(f"Output: {res}")
        
        assert spec1(nums, target, res), "Spec 1 failed"
        assert spec2(nums, target, res), "Spec 2 failed"
        assert spec3(nums, target, res), "Spec 3 failed"
        assert spec4(nums, target, res), "Spec 4 failed"
        assert spec5_corrected(nums, target, res), "Spec 5 failed"
        
        print("✅ All specs passed\n")
    
    print(f"Accuracy: {CORRECT}/{TOTAL_GENERATED} = {ACCURACY*100}%")
