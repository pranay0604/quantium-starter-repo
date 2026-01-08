#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Activate virtual environment
source venv/bin/activate

# Run test suite
python -m pytest

# If tests pass, exit with code 0
exit 0
