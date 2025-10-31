# Week 5 - Unit Tests

## 📖 Overview

Week 5 focuses on unit testing - writing code to test your code. You'll learn how to use pytest to write automated tests that verify your functions work correctly, helping you catch bugs early and maintain code quality.

## 🎯 Learning Objectives

- Understand the importance of testing
- Write unit tests with pytest
- Use assertions to verify expected behavior
- Test edge cases and error conditions
- Use `pytest.raises()` for exception testing
- Organize tests effectively
- Practice test-driven development (TDD)

## 📝 Problem Sets

### Testing my twttr
Write tests for the twttr program from Week 2.

**Files:**
- `ps5/twttr/twttr.py` - Function to remove vowels
- `ps5/twttr/test_twttr.py` - Unit tests

**Test cases:**
- Lowercase and uppercase vowels
- Numbers and punctuation
- Mixed cases

### Back to the Bank
Write tests for the bank program from Week 1.

**Files:**
- `ps5/bank/bank.py` - Greeting value function
- `ps5/bank/test_bank.py` - Unit tests

**Test cases:**
- "hello" returns 0
- Starts with "h" returns 20
- Other greetings return 100
- Case insensitivity

### Re-requesting a Vanity Plate
Write tests for the plates program from Week 2.

**Files:**
- `ps5/plates/plates.py` - License plate validator
- `ps5/plates/test_plates.py` - Unit tests

**Test cases:**
- Length validation (2-6 characters)
- Starting letters requirement
- Number placement rules
- Zero handling
- Special character rejection

### Refueling
Write tests for the fuel program from Week 3.

**Files:**
- `ps5/fuel/fuel.py` - Fraction converter with functions
- `ps5/fuel/test_fuel.py` - Unit tests

**Test cases:**
- Valid fractions
- Zero division
- Invalid input
- Gauge output (E, F, percentage)

## 🔍 Key Concepts

### Basic Test Structure
```python
# test_calculator.py
from calculator import square

def test_square_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_square_zero():
    assert square(0) == 0
```

### Testing Exceptions
```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
```

### Multiple Assertions
```python
def test_multiple_cases():
    assert function("input1") == "output1"
    assert function("input2") == "output2"
    assert function("input3") == "output3"
```

### Test Organization
```python
# Group related tests
def test_positive_numbers():
    assert is_valid(5) == True
    assert is_valid(100) == True

def test_negative_numbers():
    assert is_valid(-5) == False
    assert is_valid(-100) == False
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific file
pytest test_calculator.py

# Verbose output
pytest -v

# Show print statements
pytest -s

# Run specific test function
pytest test_calculator.py::test_square_positive
```

## 💡 Tips

1. **Test edge cases** - empty strings, zero, negative numbers, etc.
2. **One test per concept** - Keep tests focused
3. **Descriptive names** - `test_negative_input` not `test1`
4. **Test expected failures** - Use `pytest.raises()`
5. **Run tests frequently** - Catch bugs early
6. **Test before fixing** - Write a failing test, then fix the code
7. **Keep tests independent** - Each test should run in isolation

## 📚 Additional Resources

- [pytest Documentation](https://docs.pytest.org/)
- [Testing Best Practices](https://realpython.com/pytest-python-testing/)
- [Test-Driven Development](https://testdriven.io/test-driven-development/)

## ▶️ Running the Code

```bash
# Navigate to a problem directory
cd week5/ps5/twttr

# Run tests
pytest test_twttr.py

# Run with verbose output
pytest test_twttr.py -v

# Run with coverage
pytest test_twttr.py --cov=twttr
```

## 🧪 Test Example: Bank

```python
# test_bank.py
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello, world") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey there") == 20
    assert value("How are you?") == 20

def test_other():
    assert value("good morning") == 100
    assert value("What's up?") == 100
```

## 📋 Test Output Example

```
============================= test session starts ==============================
collected 3 items

test_bank.py::test_hello PASSED                                          [ 33%]
test_bank.py::test_h PASSED                                              [ 66%]
test_bank.py::test_other PASSED                                          [100%]

============================== 3 passed in 0.01s ===============================
```

## 🎯 Testing Checklist

- [ ] Test typical inputs
- [ ] Test edge cases (empty, zero, max values)
- [ ] Test invalid inputs
- [ ] Test expected exceptions
- [ ] Test boundary conditions
- [ ] All test names are descriptive
- [ ] Tests are independent
- [ ] All tests pass

## 🔧 Common pytest Commands

```bash
# Run all tests
pytest

# Stop at first failure
pytest -x

# Run last failed tests
pytest --lf

# Show coverage report
pytest --cov=. --cov-report=html

# Run tests matching pattern
pytest -k "test_hello"

# Show local variables in traceback
pytest -l
```

## 💻 Refactoring for Testing

**Before (not testable):**
```python
def main():
    name = input("Name: ")
    print(f"Hello, {name}")

main()
```

**After (testable):**
```python
def main():
    name = input("Name: ")
    print(hello(name))

def hello(name="World"):
    return f"Hello, {name}"

if __name__ == "__main__":
    main()
```

---

[← Previous Week](../week4/README.md) | [Back to Main](../../README.md) | [Next Week →](../week6/README.md)
