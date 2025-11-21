# Exercise 3 - Requirements Checklist

## Assignment Requirements Verification

### ✅ Part 1: Generate, Evaluate, and Refine Specifications (5 pts)

#### Required Deliverables:

- [x] **LLM prompt** for specification generation
  - Location: `README.md` → "Prompts Used" section
  - File: Lines showing exact prompts used

- [x] **Generated assertions before correction**
  - Location: `specs/two_sum_specs.py` → "LLM GENERATED SPECS (Original)" section
  - Location: `specs/palindrome_specs.py` → "LLM GENERATED SPECS (Original)" section

- [x] **Accuracy rate calculation**
  - Two Sum: 4/5 = 80% (in `specs/two_sum_specs.py`)
  - Palindrome: 4/5 = 80% (in `specs/palindrome_specs.py`)
  - Overall: 8/10 = 80% (in `README.md`)

- [x] **Table of incorrect assertions**
  - Location: `README.md` → "Part 1 Results" section
  - Shows issue and corrected version for each incorrect spec

- [x] **Issues documented for each incorrect assertion**
  - Two Sum Spec 5: Self-reference violation
  - Palindrome Spec 4: Self-reference + side effect (random import)
  - Documented in both `specs/*.py` files and `README.md`

- [x] **Corrected assertions**
  - Location: `specs/two_sum_specs.py` → "CORRECTED SPECIFICATIONS" section
  - Location: `specs/palindrome_specs.py` → "CORRECTED SPECIFICATIONS" section

### ✅ Part 2: Use Specifications to Guide Test Improvement (5 pts)

#### Required Deliverables:

- [x] **LLM prompt used to generate test cases**
  - Location: `README.md` → "Part 2 - Test Generation" under "Prompts Used"
  - Includes corrected specifications fed to LLM

- [x] **List of resulting tests labeled as spec-guided**
  - Location: `tests/test_spec_guided.py`
  - 16 tests total, all prefixed with `test_spec_guided_`
  - Each test has docstring explaining which specs it validates

- [x] **Before/after coverage table**
  - Location: `README.md` → "Coverage Comparison" section
  - Location: `coverage_results.md` → "Coverage Comparison Table"
  - Shows Old Stmt %, New Stmt %, Old Branch %, New Branch %

- [x] **Case-specific insight per problem**
  - Two Sum insight: `README.md` and `coverage_results.md`
  - Palindrome insight: `README.md` and `coverage_results.md`
  - Both explain why coverage stayed at 100% but quality improved

### ✅ Repository Requirements

#### Required in GitHub Repository:

- [x] **Source code of the problems**
  - Location: `src/solutions.py`
  - Contains: `two_sum()` and `is_palindrome()`

- [x] **Test files (baseline + improved)**
  - Baseline: `tests/test_baseline.py` (19 tests from Exercise 2)
  - Improved: `tests/test_spec_guided.py` (16 new spec-guided tests)
  - Combined runner: Can run all with `pytest tests/`

- [x] **Scripts/config for coverage**
  - Script: `run_coverage.sh` (automated coverage runner)
  - Config: `pytest.ini` (pytest configuration)
  - Config: `.coveragerc` settings in `pytest.ini`

- [x] **Generated and revised assertions**
  - Generated (original): `specs/two_sum_specs.py` and `specs/palindrome_specs.py`
  - Revised (corrected): Same files, "CORRECTED SPECIFICATIONS" sections
  - Evaluation: Accuracy rates and issues documented

- [x] **Generated coverage reports (HTML/XML)**
  - HTML Baseline: `coverage_reports/baseline_html/index.html`
  - HTML Improved: `coverage_reports/improved_html/index.html`
  - XML Baseline: `coverage_reports/baseline_coverage.xml`
  - XML Improved: `coverage_reports/improved_coverage.xml`

- [x] **Instructions to reproduce locally**
  - Location: `REPRODUCE.md` (comprehensive step-by-step guide)
  - Location: `README.md` → "Running Tests & Coverage" section
  - Includes troubleshooting section

### ✅ PDF Report Requirements

The repository contains all content needed for the PDF report:

- [x] Part 1 prompts → `README.md`
- [x] Part 1 generated specs → `specs/*.py` files
- [x] Part 1 accuracy table → `README.md`
- [x] Part 1 corrections table → `README.md` and `specs/*.py`
- [x] Part 2 prompts → `README.md`
- [x] Part 2 generated tests → `tests/test_spec_guided.py`
- [x] Part 2 coverage table → `README.md` and `coverage_results.md`
- [x] Part 2 case insights → `README.md` and `coverage_results.md`
- [x] GitHub repository link → To be added by student

## File Inventory

### Source Code (2 files)
- `src/solutions.py` - Problem implementations
- `src/__init__.py` - Package init

### Tests (3 files)
- `tests/test_baseline.py` - 19 baseline tests
- `tests/test_spec_guided.py` - 16 spec-guided tests
- `tests/__init__.py` - Package init

### Specifications (3 files)
- `specs/two_sum_specs.py` - Two Sum specifications + analysis
- `specs/palindrome_specs.py` - Palindrome specifications + analysis
- `specs/__init__.py` - Package init

### Coverage Reports (4 files)
- `coverage_reports/baseline_html/index.html` - Baseline HTML report
- `coverage_reports/improved_html/index.html` - Improved HTML report
- `coverage_reports/baseline_coverage.xml` - Baseline XML report
- `coverage_reports/improved_coverage.xml` - Improved XML report

### Configuration & Scripts (4 files)
- `run_coverage.sh` - Automated coverage script
- `pytest.ini` - Pytest configuration
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore rules

### Documentation (4 files)
- `README.md` - Main documentation with all results
- `coverage_results.md` - Detailed coverage analysis
- `REPRODUCE.md` - Step-by-step reproduction guide
- `QUICK_REFERENCE.md` - Quick reference card

**Total: 23 files**

## Verification Commands

Run these to verify everything works:

```bash
# 1. Check all files exist
ls -R

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run baseline tests
pytest tests/test_baseline.py -v

# 4. Run all tests
pytest tests/ -v

# 5. Generate coverage
./run_coverage.sh

# 6. Verify specifications
python specs/two_sum_specs.py
python specs/palindrome_specs.py

# 7. Check coverage reports exist
ls coverage_reports/baseline_html/index.html
ls coverage_reports/improved_html/index.html
ls coverage_reports/*.xml
```

## Assignment Compliance Score

| Requirement Category | Status | Files/Evidence |
|---------------------|--------|----------------|
| Part 1: LLM Prompts | ✅ Complete | README.md |
| Part 1: Generated Specs | ✅ Complete | specs/*.py |
| Part 1: Accuracy Rate | ✅ Complete | specs/*.py, README.md |
| Part 1: Corrections | ✅ Complete | specs/*.py, README.md |
| Part 2: Test Prompts | ✅ Complete | README.md |
| Part 2: Spec-Guided Tests | ✅ Complete | tests/test_spec_guided.py |
| Part 2: Coverage Table | ✅ Complete | README.md, coverage_results.md |
| Part 2: Case Insights | ✅ Complete | README.md, coverage_results.md |
| Source Code | ✅ Complete | src/solutions.py |
| Test Files | ✅ Complete | tests/*.py |
| Coverage Scripts | ✅ Complete | run_coverage.sh, pytest.ini |
| Coverage Reports | ✅ Complete | coverage_reports/* |
| Reproduction Guide | ✅ Complete | REPRODUCE.md |

**Overall: 13/13 Requirements Met ✅**

## Ready for Submission

This repository is **100% complete** and meets all assignment requirements:

✅ All Part 1 deliverables present  
✅ All Part 2 deliverables present  
✅ All repository requirements present  
✅ Coverage reports (HTML + XML) included  
✅ Reproduction instructions included  
✅ Scripts and configuration included  

**Status: READY TO PUSH TO GITHUB** 🚀
