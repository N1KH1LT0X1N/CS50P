# Week 9 - Et Cetera

## 📖 Overview

Week 9 wraps up the course with additional Python features and concepts. This includes sets, global variables, type hints, docstrings, argument unpacking, list/dict comprehensions, generators, and the culmination of your learning: the **Final Project**.

## 🎯 Learning Objectives

- Use sets for unique collections
- Understand global vs local scope
- Add type hints for better code documentation
- Write comprehensive docstrings
- Use `*args` and `**kwargs`
- Master comprehensions for concise code
- Create generators with `yield`
- Design and implement a complete project
- Apply all CS50P concepts in a real application

## 📝 Problem Sets

### Final Project
Your capstone project that demonstrates everything you've learned in CS50P!

**Location:** `ps9/finalproject/`

**Requirements:**
- Must be in Python
- Must be more complex than previous problem sets
- Should have a `main()` function
- Include a `README.md` explaining your project
- Include a `requirements.txt` if using libraries
- Recommended: Include tests
- Video demonstration required

**Project Ideas:**
- Web scraper with data analysis
- Interactive game
- API wrapper or client
- Data visualization tool
- Automation script
- CLI application
- File processor
- Machine learning application
- Discord/Slack bot
- Personal productivity tool

## 🔍 Key Concepts

### Sets
```python
# Create a set (unique elements)
students = set()
students.add("Harry")
students.add("Ron")
students.add("Hermione")
students.add("Harry")  # Won't be added again

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2        # {1, 2, 3, 4, 5}
intersection = set1 & set2  # {3}
difference = set1 - set2    # {1, 2}
```

### Global Variables
```python
balance = 0  # Global

def deposit(n):
    global balance  # Declare global
    balance += n

def main():
    deposit(100)
    print(balance)  # 100
```

### Type Hints
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(x: int, y: int) -> int:
    return x + y

# With collections
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

# Optional types
from typing import Optional

def find_student(name: str) -> Optional[Student]:
    # Returns Student or None
    pass
```

### Docstrings
```python
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values
    
    Returns:
        float: The arithmetic mean of the numbers
    
    Raises:
        ValueError: If the list is empty
    
    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)
```

### Args and Kwargs
```python
# Variable positional arguments
def total(*args):
    return sum(args)

print(total(1, 2, 3))  # 6
print(total(1, 2, 3, 4, 5))  # 15

# Variable keyword arguments
def student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student(name="Harry", house="Gryffindor", year=1)
```

### Unpacking
```python
# List unpacking
def total(galleons, sickles, knuts):
    return galleons * 17 * 29 + sickles * 29 + knuts

coins = [100, 50, 25]
print(total(*coins))  # Unpacks list

# Dictionary unpacking
def student(name, house, year):
    return f"{name}, {house}, Year {year}"

info = {"name": "Harry", "house": "Gryffindor", "year": 1}
print(student(**info))  # Unpacks dict
```

### List Comprehensions
```python
# Traditional loop
squares = []
for i in range(10):
    squares.append(i ** 2)

# List comprehension
squares = [i ** 2 for i in range(10)]

# With condition
evens = [i for i in range(20) if i % 2 == 0]

# Nested
matrix = [[i * j for j in range(3)] for i in range(3)]
```

### Dictionary Comprehensions
```python
# Create dict from lists
names = ["Harry", "Ron", "Hermione"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor"]
students = {name: house for name, house in zip(names, houses)}

# Transform dict
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
doubled = {fruit: price * 2 for fruit, price in prices.items()}

# Filter dict
expensive = {k: v for k, v in prices.items() if v > 1.0}
```

### Generators
```python
# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)  # 5, 4, 3, 2, 1

# Generator expression
squares = (i ** 2 for i in range(1000000))  # Memory efficient!

# Infinite generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

## 💡 Tips for Final Project

1. **Start simple** - Get basic functionality working first
2. **Plan ahead** - Write a design document or pseudocode
3. **Test incrementally** - Don't write everything before testing
4. **Use version control** - Commit frequently
5. **Document as you go** - Write docstrings and comments
6. **Handle errors** - Use try-except appropriately
7. **Follow style guide** - Keep code clean and readable
8. **Ask for help** - Use CS50 community resources
9. **Be creative** - Make something you're passionate about
10. **Have fun!** - This is your chance to build something cool

## 📚 Additional Resources

- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Python Generators](https://wiki.python.org/moin/Generators)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [CS50P Final Project Guidance](https://cs50.harvard.edu/python/2022/project/)

## 📋 Final Project Checklist

- [ ] Project idea selected
- [ ] Basic functionality implemented
- [ ] `main()` function created
- [ ] Error handling added
- [ ] `README.md` written with:
  - [ ] Project title
  - [ ] Description
  - [ ] How to install/run
  - [ ] Features
  - [ ] Technologies used
- [ ] `requirements.txt` created (if needed)
- [ ] Tests written (recommended)
- [ ] Code is well-documented
- [ ] Video demonstration recorded
- [ ] Project tested thoroughly

## 🎬 Video Requirements

Your video should:
- Be at most 3 minutes long
- Demonstrate your project's functionality
- Show your code structure
- Explain key design decisions
- Be uploaded to YouTube (unlisted or public)

## 💻 Example Final Project Structure

```
finalproject/
├── project.py          # Main program
├── test_project.py     # Unit tests
├── README.md           # Project documentation
├── requirements.txt    # Dependencies
├── data/              # Data files (if needed)
├── assets/            # Images, etc. (if needed)
└── config.py          # Configuration (if needed)
```

## 🎓 Final Project README Template

```markdown
# Project Title

## Video Demo: <URL>

## Description
[Detailed description of your project]

## Features
- Feature 1
- Feature 2
- Feature 3

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python project.py
```

## Technologies
- Python 3.11
- Library 1
- Library 2

## Design Decisions
[Explain key design choices]

## Future Improvements
[What you'd add given more time]
```

## 🚀 Advanced Concepts Summary

### Type Hints Best Practices
```python
from typing import List, Dict, Optional, Union

def process_data(
    data: List[Dict[str, Union[int, str]]],
    filters: Optional[List[str]] = None
) -> Dict[str, int]:
    """Process data with optional filters."""
    pass
```

### Generator Pipeline
```python
def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip()

def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

def process_logs(filename, keyword):
    lines = read_file(filename)
    filtered = filter_lines(lines, keyword)
    return list(filtered)
```

### Context Managers
```python
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.end = time.time()
        print(f"Elapsed: {self.end - self.start}s")

with Timer():
    # Code to time
    pass
```

## 🎉 Congratulations!

You've reached the end of CS50P! Now it's time to apply everything you've learned in your final project. Good luck, and happy coding! 🚀

---

[← Previous Week](../week8/README.md) | [Back to Main](../../README.md)
