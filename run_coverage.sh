#!/bin/bash

# Coverage Analysis Script for Exercise 3
# Generates HTML and XML coverage reports

set -e

echo "=========================================="
echo "Exercise 3 - Coverage Analysis"
echo "=========================================="
echo ""

# Check if pytest and coverage are installed
if ! python -m pytest --version > /dev/null 2>&1; then
    echo "ERROR: pytest not installed. Run: pip install -r requirements.txt"
    exit 1
fi

# Create coverage_reports directory
mkdir -p coverage_reports

echo "Step 1: Running baseline tests (Exercise 2)..."
python -m pytest tests/test_baseline.py \
    --cov=src \
    --cov-report=html:coverage_reports/baseline_html \
    --cov-report=xml:coverage_reports/baseline_coverage.xml \
    --cov-report=term \
    -v

echo ""
echo "✓ Baseline coverage reports generated:"
echo "  - HTML: coverage_reports/baseline_html/index.html"
echo "  - XML:  coverage_reports/baseline_coverage.xml"
echo ""

echo "Step 2: Running all tests (baseline + spec-guided)..."
python -m pytest tests/ \
    --cov=src \
    --cov-report=html:coverage_reports/improved_html \
    --cov-report=xml:coverage_reports/improved_coverage.xml \
    --cov-report=term \
    -v

echo ""
echo "✓ Improved coverage reports generated:"
echo "  - HTML: coverage_reports/improved_html/index.html"
echo "  - XML:  coverage_reports/improved_coverage.xml"
echo ""

echo "=========================================="
echo "Coverage Analysis Complete!"
echo "=========================================="
echo ""
echo "View reports:"
echo "  Baseline:  open coverage_reports/baseline_html/index.html"
echo "  Improved:  open coverage_reports/improved_html/index.html"
echo ""
