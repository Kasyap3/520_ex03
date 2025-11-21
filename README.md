# Exercise 3 - Specification-Guided Test Generation

**Student:** Kasyap Varanasi  
**Date:** November 20, 2025  
**GitHub:** https://github.com/Kasyap3/520_ex03

## Structure
```
├── src/solutions.py           # Two Sum & Palindrome
├── tests/
│   ├── test_baseline.py       # Exercise 2 tests (19 tests)
│   └── test_spec_guided.py    # Part 2 tests (16 new tests)
├── specs/
│   ├── two_sum_specs.py       # Part 1 specs (80% accuracy)
│   └── palindrome_specs.py    # Part 1 specs (80% accuracy)
├── coverage_results.md        # Coverage comparison
└── requirements.txt
```

## Quick Setup

```bash
pip install -r requirements.txt
python -m pytest tests/test_baseline.py -v
python -m pytest tests/ -v
```

## Part 1 Results: Specification Generation

### Two Sum Specifications

**Accuracy:** 4/5 correct = **80%**

✅ **Correct Specs (4):**
1. Result type must be list
2. Length must be 0 or 2
3. Valid array indices
4. Different indices (no reuse)

❌ **Incorrect Spec (1):**
5. Called `two_sum()` in assertion (self-reference)

**Corrected:** Check `nums[res[0]] + nums[res[1]] == target` directly

### Palindrome Specifications

**Accuracy:** 4/5 correct = **80%**

✅ **Correct Specs (4):**
1. Result type must be boolean
2. Empty string returns True
3. Single character returns True
5. Non-alphanumeric ignored

❌ **Incorrect Spec (1):**
4. Called `is_palindrome()` multiple times (self-reference) + imported random

**Corrected:** Check filtered string property directly

### Overall Part 1 Accuracy

| Problem | Total | Correct | Incorrect | Accuracy |
|---------|-------|---------|-----------|----------|
| Two Sum | 5 | 4 | 1 | 80% |
| Palindrome | 5 | 4 | 1 | 80% |
| **Combined** | **10** | **8** | **2** | **80%** |

**Common Issue:** Both incorrect specs involved self-reference (calling the function being specified)

## Part 2 Results: Test Generation

### Generated Tests Summary

**Two Sum:** 8 spec-guided tests
- `test_spec_guided_two_sum_type_check` - Validates Spec 1
- `test_spec_guided_two_sum_length` - Validates Spec 2
- `test_spec_guided_two_sum_valid_indices` - Validates Spec 3
- `test_spec_guided_two_sum_different_indices` - Validates Spec 4
- `test_spec_guided_two_sum_correct_sum` - Validates Spec 5
- `test_spec_guided_two_sum_edge_empty` - Validates Specs 1, 2
- `test_spec_guided_two_sum_edge_single` - Validates Specs 1, 2
- `test_spec_guided_two_sum_negative_target` - Validates Specs 1, 2, 4, 5

**Palindrome:** 8 spec-guided tests
- `test_spec_guided_palindrome_type_check` - Validates Spec 1
- `test_spec_guided_palindrome_empty_string` - Validates Spec 2
- `test_spec_guided_palindrome_single_char` - Validates Spec 3
- `test_spec_guided_palindrome_case_insensitive` - Validates Spec 4
- `test_spec_guided_palindrome_ignore_special` - Validates Spec 5
- `test_spec_guided_palindrome_numbers_only` - Validates Specs 1, 5
- `test_spec_guided_palindrome_mixed_special_chars` - Validates Spec 5
- `test_spec_guided_palindrome_not_palindrome` - Validates Specs 1, 4, 5

**Total:** 16 new spec-guided tests

## Coverage Comparison

See `coverage_results.md` for detailed comparison.

### Summary

| Problem | Baseline Tests | Baseline Stmt % | With Spec Tests | Improved Stmt % | Change |
|---------|----------------|-----------------|-----------------|-----------------|--------|
| Two Sum | 8 | 98.8% | 16 | 98.8% | 0% |
| Palindrome | 11 | 97.6% | 19 | 97.6% | 0% |
| **Overall** | **19** | **98.2%** | **35** | **98.2%** | **0%** |

### Insights

**Two Sum:**
- Coverage remained at 98.8% because baseline tests already covered all reachable code paths
- Spec-guided tests improved test quality by explicitly validating formal properties (type, length, validity)
- Tests now serve as executable documentation of the function's contract

**Palindrome:**
- Coverage remained at 97.6% (already saturated)
- Spec-guided tests added systematic validation of case-insensitivity and special character handling
- Better edge case coverage for empty strings and single characters

**Key Finding:** Specifications guided creation of more rigorous tests that validate logical correctness properties, even when coverage metrics don't increase.

## Prompts Used

### Part 1 - Spec Generation

```
Problem: Given an array of integers nums and an integer target, 
return indices of the two numbers that add up to target.

Method signature: def two_sum(nums: List[int], target: int) -> List[int]

Generate 5 formal specifications as assertions. Let 'res' be the return value.
Requirements:
- Do NOT call two_sum() in assertions
- NO side effects (print, I/O, random)
- Pure logic only
- Express relationship between nums, target, and res
```

### Part 2 - Test Generation

```
Generate pytest test cases that validate these corrected specifications:

Two Sum Specs:
1. isinstance(res, list)
2. len(res) == 0 or len(res) == 2
3. len(res) == 0 or (0 <= res[0] < len(nums) and 0 <= res[1] < len(nums))
4. len(res) == 0 or res[0] != res[1]
5. len(res) == 0 or nums[res[0]] + nums[res[1]] == target

Generate 5-8 tests. Prefix with test_spec_guided_*
Include comments showing which spec each validates.
```

## Running Tests & Coverage

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run automated coverage analysis
./run_coverage.sh
```

This generates HTML and XML coverage reports in `coverage_reports/`.

### Manual Commands

```bash
# Baseline only
pytest tests/test_baseline.py -v

# All tests  
pytest tests/ -v

# With coverage (baseline)
pytest tests/test_baseline.py --cov=src --cov-report=html:coverage_reports/baseline_html --cov-report=term

# With coverage (improved)
pytest tests/ --cov=src --cov-report=html:coverage_reports/improved_html --cov-report=term
```

### View Coverage Reports

**HTML Reports (already generated):**
- Baseline: `coverage_reports/baseline_html/index.html`
- Improved: `coverage_reports/improved_html/index.html`

**XML Reports (already generated):**
- Baseline: `coverage_reports/baseline_coverage.xml`
- Improved: `coverage_reports/improved_coverage.xml`

See `REPRODUCE.md` for detailed instructions to regenerate reports locally.

## Key Takeaways

1. **Specification Accuracy:** 80% - LLM struggles with self-reference violations
2. **Coverage:** No change, but test quality improved significantly
3. **Test Documentation:** Spec-guided tests explicitly state what properties they validate
4. **Formal Methods:** Specifications help catch logical errors even at high coverage
