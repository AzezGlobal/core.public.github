#!/bin/bash
# Build script for Python components

set -e

echo "Building Core Public GitHub - Python Components"
echo "==============================================="

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run linting
echo "Running linters..."
echo "  - black (code formatter)"
black --check src/main/ src/test/ || echo "Run 'black src/' to format code"

echo "  - flake8 (style checker)"
flake8 src/main/ src/test/ --max-line-length=120 || echo "Fix flake8 issues"

echo "  - isort (import sorter)"
isort --check-only src/main/ src/test/ || echo "Run 'isort src/' to sort imports"

# Type checking
echo "Running type checking..."
mypy src/main/ --ignore-missing-imports || echo "Fix type issues"

# Run tests
echo "Running tests..."
pytest src/test/ -v --cov=src/main/ --cov-report=term-missing --cov-report=html

echo ""
echo "Build completed!"
echo "Coverage report: htmlcov/index.html"
