# Week 2 - Loops

## 📖 Overview

Week 2 introduces loops - a powerful programming concept that allows you to repeat code efficiently. You'll learn about `while` loops, `for` loops, and how to iterate through sequences.

## 🎯 Learning Objectives

- Understand and implement `while` loops
- Use `for` loops to iterate through sequences
- Work with lists and ranges
- Control loop flow with `break` and `continue`
- Handle user input validation with loops
- Implement iteration patterns

## 📝 Problem Sets

### camelCase
Convert camelCase variable names to snake_case - string manipulation with iteration.

**File:** `ps2/camel/camel.py`

**Example:** `camelCase` → `camel_case`

### Coke Machine
Simulate a Coke vending machine that accepts only certain coins - loop-based transaction handling.

**File:** `ps2/coke/coke.py`

**Details:**
- Cost: 50 cents
- Accepts: 25¢, 10¢, 5¢ coins
- Provides change

### Nutrition Facts
Look up calories for fruits - working with dictionaries and user input.

**File:** `ps2/nutrition/nutrition.py`

### Vanity Plates
Validate custom license plates according to specific rules - complex string validation.

**File:** `ps2/plates/plates.py`

**Rules:**
- Length: 2-6 characters
- Must start with at least 2 letters
- Numbers must come at the end
- First number cannot be 0
- No periods, spaces, or punctuation

**Tests:** `test_plates.py`

### Just setting up my twttr
Remove vowels from text (like early Twitter) - string filtering.

**File:** `ps2/twttr/twttr.py`

**Tests:** `test_twttr.py`

## 🔍 Key Concepts

### While Loops
```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Input validation
while True:
    n = int(input("Positive number: "))
    if n > 0:
        break
```

### For Loops
```python
# Iterate over range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate over string
for char in "Hello":
    print(char)

# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Loop Control
```python
# break - exit loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
```

### Lists
```python
# Create a list
numbers = [1, 2, 3, 4, 5]

# Append to list
numbers.append(6)

# List comprehension
squares = [x**2 for x in range(5)]
```

## 💡 Tips

1. **Avoid infinite loops** - ensure loop conditions eventually become False
2. **Use `for` loops** when you know iteration count, `while` for unknown
3. **Validate user input** with loops to ensure correct data
4. **Use `enumerate()`** when you need both index and value
5. **List comprehensions** can make code more concise and readable

## 📚 Additional Resources

- [Python Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
- [Break and Continue](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)

## ▶️ Running the Code

```bash
# Navigate to a problem directory
cd week2/ps2/plates

# Run the script
python plates.py

# Run tests
pytest test_plates.py -v
```

## 🧪 Testing Example

```python
# test_plates.py
from plates import is_valid

def test_length():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("TOOLONG") == False

def test_starts_with_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False

def test_numbers_end():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False

def test_first_number():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
```

---

[← Previous Week](../week1/README.md) | [Back to Main](../../README.md) | [Next Week →](../week3/README.md)
