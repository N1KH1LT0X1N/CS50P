# Week 1 - Conditionals

## 📖 Overview

Week 1 dives into conditional logic - the ability to make decisions in your code. You'll learn about comparison operators, boolean expressions, and how to control program flow with `if`, `elif`, and `else` statements.

## 🎯 Learning Objectives

- Write conditional statements using `if`, `elif`, and `else`
- Use comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Understand boolean logic (`and`, `or`, `not`)
- Chain multiple conditions
- Apply conditional logic to solve problems
- Use the `match` statement (Python 3.10+)

## 📝 Problem Sets

### Deep Thought
Check if the answer to the Great Question is correct - simple conditional logic.

**File:** `ps1/deep/deep.py`

### Home Federal Savings Bank
Implement a greeting-based payment system - working with string methods and conditionals.

**File:** `ps1/bank/bank.py`

**Rules:**
- Greeting starts with "hello" → $0
- Greeting starts with "h" (but not "hello") → $20
- Otherwise → $100

### File Extensions
Determine media type from file extension - practicing string methods with conditionals.

**File:** `ps1/extensions/extensions.py`

**Extensions:** `.gif`, `.jpg`, `.jpeg`, `.png`, `.pdf`, `.txt`, `.zip`

### Math Interpreter
Evaluate simple arithmetic expressions - parsing user input and performing calculations.

**File:** `ps1/interpreter/interpreter.py`

**Operations:** Addition, Subtraction, Multiplication, Division

### Meal Time
Determine meal type based on time - working with time comparisons.

**File:** `ps1/meal/meal.py`

**Times:**
- Breakfast: 7:00 - 8:00
- Lunch: 12:00 - 13:00
- Dinner: 18:00 - 19:00

## 🔍 Key Concepts

### If Statements
```python
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if all conditions are False
```

### Comparison Operators
```python
x == y  # Equal to
x != y  # Not equal to
x > y   # Greater than
x < y   # Less than
x >= y  # Greater than or equal to
x <= y  # Less than or equal to
```

### Boolean Logic
```python
# AND - both conditions must be True
if age >= 18 and has_license:
    print("Can drive")

# OR - at least one condition must be True
if is_weekend or is_holiday:
    print("No work today!")

# NOT - negates the condition
if not is_raining:
    print("Go outside")
```

### Match Statements (Python 3.10+)
```python
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
```

## 💡 Tips

1. **Use `lower()` or `upper()`** for case-insensitive comparisons
2. **Order matters** in `elif` chains - more specific conditions first
3. **Use `in` operator** to check substring presence
4. **Keep conditions simple** - break complex logic into multiple conditions
5. **Remember operator precedence** - use parentheses for clarity

## 📚 Additional Resources

- [Python Conditionals](https://docs.python.org/3/tutorial/controlflow.html)
- [Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Python Match Statement](https://peps.python.org/pep-0636/)

## ▶️ Running the Code

```bash
# Navigate to a problem directory
cd week1/ps1/bank

# Run the script
python bank.py

# Run tests (if available)
pytest test_bank.py
```

## 🧪 Testing Example

```python
# test_bank.py
from bank import greet

def test_hello():
    assert greet("hello") == 0
    assert greet("hello, world") == 0

def test_h():
    assert greet("hi") == 20
    assert greet("hey there") == 20

def test_other():
    assert greet("good morning") == 100
```

---

[← Previous Week](../week0/README.md) | [Back to Main](../../README.md) | [Next Week →](../week2/README.md)
