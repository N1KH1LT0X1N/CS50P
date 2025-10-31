# Week 0 - Functions, Variables

## 📖 Overview

Week 0 introduces the fundamental building blocks of Python programming: functions and variables. You'll learn how to create your first Python programs, work with different data types, and write your own functions.

## 🎯 Learning Objectives

- Understand Python syntax and basic structure
- Work with variables and data types (strings, integers, floats)
- Use built-in functions like `print()` and `input()`
- Create custom functions
- Format strings and output
- Perform basic arithmetic operations

## 📝 Problem Sets

### Indoor Voice
Convert user input to lowercase - practicing string manipulation and the `lower()` method.

**File:** `ps0/indoor/indoor.py`

### Playback
Replace spaces in a sentence with "..." - working with string methods.

**File:** `ps0/playback/playback.py`

### Faces
Convert emoticons to emoji - introduction to string replacement.

**File:** `ps0/faces/faces.py`

### Einstein
Calculate energy using Einstein's famous equation E=mc² - working with mathematical operations.

**File:** `ps0/einstein/einstein.py`

**Formula:** E = m × c²
- Where c (speed of light) = 300,000,000 m/s

### Tip Calculator
Calculate tip and total amount for a meal - practicing arithmetic and formatting.

**File:** `ps0/tip/tip.py`

## 🔍 Key Concepts

### Variables
```python
# Assignment
name = "World"
age = 25
price = 19.99
```

### Functions
```python
# Built-in functions
print("Hello, World!")
name = input("What's your name? ")

# Custom functions
def hello(name="World"):
    print(f"Hello, {name}!")
```

### String Formatting
```python
# f-strings (recommended)
print(f"Hello, {name}!")

# format method
print("Hello, {}!".format(name))

# % operator (older style)
print("Hello, %s!" % name)
```

## 💡 Tips

1. **Use descriptive variable names** - Make your code readable
2. **Follow PEP 8** - Python's style guide
3. **Practice with `input()` and `print()`** - Get comfortable with I/O
4. **Experiment in the Python REPL** - Test code snippets interactively

## 📚 Additional Resources

- [Python Documentation - Data Types](https://docs.python.org/3/library/stdtypes.html)
- [Python f-strings](https://realpython.com/python-f-strings/)
- [PEP 8 Style Guide](https://pep8.org/)

## ▶️ Running the Code

```bash
# Navigate to a problem directory
cd week0/ps0/einstein

# Run the script
python einstein.py
```

---

[← Back to Main](../../README.md) | [Next Week →](../week1/README.md)
