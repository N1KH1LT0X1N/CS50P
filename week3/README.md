# Week 3 - Exceptions

## 📖 Overview

Week 3 introduces exception handling in Python - a crucial skill for writing robust programs that can gracefully handle errors. You'll learn how to catch, handle, and raise exceptions to prevent your programs from crashing unexpectedly.

## 🎯 Learning Objectives

- Understand what exceptions are and why they occur
- Use `try` and `except` to catch and handle exceptions
- Implement `else` and `finally` clauses
- Raise exceptions with `raise`
- Create programs that validate user input
- Handle multiple types of exceptions

## 📝 Problem Sets

### Fuel Gauge
Convert fractions to percentages with error handling - validating user input and handling division errors.

**Files:** 
- `ps3/fuel/fuel.py`
- `ps3/fuel/test_fuel.py`

**Requirements:**
- Prompt user for fraction (X/Y)
- Handle invalid input (non-integers, Y=0, X>Y)
- Output percentage or E (≤1%) or F (≥99%)

### Felipe's Taqueria
Simulate a taqueria menu with running total - handling KeyError for invalid items.

**File:** `ps3/taqueria/taqueria.py`

**Details:**
- Display menu items and prices
- Keep running total
- Handle invalid menu items gracefully
- Exit on Control-D

### Grocery List
Create a sorted grocery list from user input - handling EOF and organizing output.

**File:** `ps3/grocery/grocery.py`

**Requirements:**
- Accept items until Control-D
- Count quantities
- Display alphabetically in uppercase

### Outdated
Convert dates from month-day-year to year-month-day format - parsing and validating dates.

**File:** `ps3/outdated/outdated.py`

**Formats:**
- Input: `9/8/1636` or `September 8, 1636`
- Output: `1636-09-08`

## 🔍 Key Concepts

### Try-Except Blocks
```python
try:
    x = int(input("x: "))
except ValueError:
    print("x is not an integer")
```

### Multiple Exceptions
```python
try:
    x = int(input("x: "))
    y = int(input("y: "))
    result = x / y
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Else Clause
```python
try:
    x = int(input("x: "))
except ValueError:
    print("Invalid input")
else:
    print(f"x is {x}")
```

### Finally Clause
```python
try:
    file = open("data.txt")
    # Process file
except FileNotFoundError:
    print("File not found")
finally:
    # Always executes
    print("Cleanup complete")
```

### Raising Exceptions
```python
def get_positive(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                raise ValueError("Must be positive")
            return n
        except ValueError as e:
            print(e)
```

### Pass Statement
```python
while True:
    try:
        x = int(input("x: "))
        break
    except ValueError:
        pass  # Silently retry
```

## 💡 Tips

1. **Be specific** with exception types - catch what you expect
2. **Use `else`** for code that should run only if no exception occurred
3. **`finally`** is perfect for cleanup (closing files, connections)
4. **Don't catch all exceptions** - `except Exception:` can hide bugs
5. **Validate early** - check input before processing
6. **Use loops** with try-except for persistent prompting

## 📚 Additional Resources

- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Exception Handling Best Practices](https://realpython.com/python-exceptions/)

## ▶️ Running the Code

```bash
# Navigate to a problem directory
cd week3/ps3/fuel

# Run the script
python fuel.py

# Run tests
pytest test_fuel.py -v
```

## 🧪 Common Exceptions

| Exception | When It Occurs |
|-----------|---------------|
| `ValueError` | Invalid value for conversion |
| `ZeroDivisionError` | Division by zero |
| `TypeError` | Wrong type for operation |
| `KeyError` | Dictionary key doesn't exist |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File doesn't exist |
| `EOFError` | Input ended unexpectedly (Control-D) |

## 🎯 Testing Example

```python
# test_fuel.py
import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("1/4") == 25

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
```

---

[← Previous Week](../week2/README.md) | [Back to Main](../../README.md) | [Next Week →](../week4/README.md)
