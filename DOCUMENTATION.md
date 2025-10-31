# CS50P Documentation

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Running Solutions](#running-solutions)
- [Testing](#testing)
- [Common Issues](#common-issues)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package manager (comes with Python)
- **Git**: [Download Git](https://git-scm.com/downloads)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/N1KH1LT0X1N/CS50P.git
cd CS50P
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
CS50P/
├── .github/
│   └── workflows/          # GitHub Actions CI/CD
├── week0/                  # Functions, Variables
│   ├── lec0/              # Lecture examples
│   └── ps0/               # Problem sets
├── week1/                  # Conditionals
├── week2/                  # Loops
├── week3/                  # Exceptions
├── week4/                  # Libraries
├── week5/                  # Unit Tests
├── week6/                  # File I/O
├── week7/                  # Regular Expressions
├── week8/                  # OOP
├── week9/                  # Et Cetera
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── pytest.ini
├── README.md
└── requirements.txt
```

## Running Solutions

### Basic Execution

Navigate to any problem directory and run the Python file:

```bash
cd week0/ps0/einstein
python einstein.py
```

### With Input

For programs that require input:

```bash
python program.py
# Then type your input when prompted
```

### Using CS50 Library

Some problems use the CS50 library:

```bash
pip install cs50
python program.py
```

## Testing

### Running Tests

This repository uses pytest for unit testing.

Run all tests:
```bash
pytest
```

Run tests for a specific week:
```bash
pytest week2/ps2/
```

Run a specific test file:
```bash
pytest week2/ps2/plates/test_plates.py
```

Run with verbose output:
```bash
pytest -v
```

Run with coverage report:
```bash
pytest --cov=. --cov-report=html
```

### Writing Tests

Example test structure:

```python
# test_example.py
from example import function_name

def test_basic_case():
    assert function_name("input") == "expected_output"

def test_edge_case():
    assert function_name("") == ""

def test_error_handling():
    with pytest.raises(ValueError):
        function_name(None)
```

## Common Issues

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'cs50'`

**Solution:**
```bash
pip install cs50
```

### Python Version Issues

**Problem:** Code doesn't work on older Python versions

**Solution:** Ensure you're using Python 3.11+
```bash
python --version
```

### Test Discovery Issues

**Problem:** pytest can't find tests

**Solution:** Ensure test files follow naming convention:
- `test_*.py` or `*_test.py`
- Test functions should start with `test_`

### Virtual Environment

**Problem:** Packages installed globally interfere with project

**Solution:** Use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Additional Resources

- [CS50P Official Website](https://cs50.harvard.edu/python/2022/)
- [Python Documentation](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/)
- [Git Documentation](https://git-scm.com/doc)

## Need Help?

- Open an issue on GitHub
- Check the [CS50 Discord](https://discord.gg/cs50)
- Review CS50P lecture notes and videos

---

Happy coding! 🚀
