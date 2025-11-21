# How to Reproduce Coverage Results Locally

This document provides step-by-step instructions to reproduce the coverage analysis on your local machine.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## Setup Instructions

### 1. Clone or Extract Repository

If from GitHub:
```bash
git clone https://github.com/Kasyap3/520_ex03
cd exercise3_minimal
```

If from archive:
```bash
tar -xzf exercise3_complete.tar.gz
cd exercise3_minimal
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- pytest>=7.0.0
- pytest-cov>=4.0.0
- coverage>=7.0.0

### 4. Verify Installation

```bash
pytest --version
# Should output: pytest 7.x.x

python -m coverage --version
# Should output: Coverage.py, version 7.x.x
```

## Running Tests

### Option 1: Use the Coverage Script (Recommended)

```bash
# Run the automated script
./run_coverage.sh
```

This will:
1. Run baseline tests with coverage
2. Run all tests (baseline + spec-guided) with coverage
3. Generate HTML and XML reports
4. Display coverage summary

**Expected Output:**
```
==========================================
Exercise 3 - Coverage Analysis
==========================================

Step 1: Running baseline tests (Exercise 2)...
[test execution output]
✓ Baseline coverage reports generated

Step 2: Running all tests (baseline + spec-guided)...
[test execution output]
✓ Improved coverage reports generated

Coverage Analysis Complete!
```

### Option 2: Manual Commands

#### Run Baseline Tests Only

```bash
python -m pytest tests/test_baseline.py \
    --cov=src \
    --cov-report=html:coverage_reports/baseline_html \
    --cov-report=xml:coverage_reports/baseline_coverage.xml \
    --cov-report=term \
    -v
```

**Expected Output:**
```
tests/test_baseline.py::test_two_sum_basic PASSED         [  5%]
tests/test_baseline.py::test_two_sum_negative PASSED      [ 10%]
[... 17 more tests ...]
======================== 19 passed in 0.12s =====================

---------- coverage: platform linux, python 3.11 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
src/__init__.py             0      0   100%
src/solutions.py           17      0   100%
-------------------------------------------
TOTAL                      17      0   100%
```

#### Run All Tests (Baseline + Spec-Guided)

```bash
python -m pytest tests/ \
    --cov=src \
    --cov-report=html:coverage_reports/improved_html \
    --cov-report=xml:coverage_reports/improved_coverage.xml \
    --cov-report=term \
    -v
```

**Expected Output:**
```
tests/test_baseline.py::test_two_sum_basic PASSED         [  2%]
[... 18 more baseline tests ...]
tests/test_spec_guided.py::test_spec_guided_two_sum_type_check PASSED [ 54%]
[... 15 more spec-guided tests ...]
======================== 35 passed in 0.18s =====================

---------- coverage: platform linux, python 3.11 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
src/__init__.py             0      0   100%
src/solutions.py           17      0   100%
-------------------------------------------
TOTAL                      17      0   100%
```

## Viewing Coverage Reports

### HTML Reports (Visual)

After running coverage:

```bash
# Open baseline report
open coverage_reports/baseline_html/index.html
# Or on Linux: xdg-open coverage_reports/baseline_html/index.html
# Or on Windows: start coverage_reports/baseline_html/index.html

# Open improved report
open coverage_reports/improved_html/index.html
```

The HTML reports show:
- Overall coverage percentage
- Per-file coverage breakdown
- Line-by-line coverage highlighting
- Uncovered lines (if any)

### XML Reports (Machine-Readable)

XML reports are located at:
- `coverage_reports/baseline_coverage.xml`
- `coverage_reports/improved_coverage.xml`

These can be imported into CI/CD tools or IDEs.

## Verifying Specifications

To verify the formal specifications work correctly:

```bash
# Verify Two Sum specifications
python specs/two_sum_specs.py

# Verify Palindrome specifications
python specs/palindrome_specs.py
```

**Expected Output:**
```
Two Sum Specification Verification:

Input: nums=[2, 7, 11, 15], target=9
Output: [0, 1]
✅ All specs passed

[... more test cases ...]

Accuracy: 4/5 = 80.0%
```

## Troubleshooting

### Issue: "pytest: command not found"

**Solution:** Make sure you installed requirements and activated virtual environment:
```bash
pip install -r requirements.txt
```

### Issue: "ModuleNotFoundError: No module named 'src'"

**Solution:** Make sure you're running from the repository root:
```bash
cd exercise3_minimal
python -m pytest tests/
```

Or set PYTHONPATH:
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python -m pytest tests/
```

### Issue: "Permission denied: ./run_coverage.sh"

**Solution:** Make the script executable:
```bash
chmod +x run_coverage.sh
./run_coverage.sh
```

### Issue: Coverage shows different percentages

**Explanation:** This is expected if you modified the source code. The provided reports show 100% coverage for the original implementation.

## Expected Results Summary

| Metric | Baseline | With Spec-Guided | Change |
|--------|----------|------------------|--------|
| Tests | 19 | 35 | +16 |
| Statement Coverage | 100% | 100% | 0% |
| Two Sum Tests | 8 | 16 | +8 |
| Palindrome Tests | 11 | 19 | +8 |

## File Locations

After running coverage, you'll find:

```
coverage_reports/
├── baseline_html/
│   └── index.html          # Baseline HTML report
├── improved_html/
│   └── index.html          # Improved HTML report
├── baseline_coverage.xml   # Baseline XML report
└── improved_coverage.xml   # Improved XML report
```

## Questions?

If you encounter any issues:
1. Check that Python 3.8+ is installed: `python --version`
2. Verify all dependencies installed: `pip list | grep pytest`
3. Make sure you're in the repository root directory
4. Try running with verbose output: `pytest -vv`

## Continuous Integration

To integrate into CI/CD pipelines:

```yaml
# Example GitHub Actions
- name: Run tests with coverage
  run: |
    pip install -r requirements.txt
    ./run_coverage.sh
    
- name: Upload coverage reports
  uses: actions/upload-artifact@v3
  with:
    name: coverage-reports
    path: coverage_reports/
```

---

**Last Updated:** November 20, 2025  
**Repository:** https://github.com/Kasyap3/520_ex03
