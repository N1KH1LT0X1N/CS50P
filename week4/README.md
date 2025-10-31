# Week 4 - Libraries

## 📖 Overview

Week 4 explores Python libraries - pre-written code that extends Python's capabilities. You'll learn how to import and use both built-in and third-party libraries to solve complex problems efficiently.

## 🎯 Learning Objectives

- Import and use Python's standard library modules
- Install and use third-party packages with pip
- Work with the `random`, `statistics`, `sys`, and `requests` modules
- Generate random numbers and make API calls
- Use command-line arguments
- Leverage existing code to build powerful programs

## 📝 Problem Sets

### Emojize
Convert emoji codes to actual emoji - using the `emoji` library.

**File:** `ps4/emojize/emojize.py`

**Example:** `:thumbs_up:` → 👍

### Frank, Ian and Glen's Letters (Figlet)
Generate ASCII art text - using the `pyfiglet` library.

**File:** `ps4/figlet/figlet.py`

**Features:**
- Random font or user-specified font
- Command-line arguments: `-f` or `--font`

### Adieu, Adieu
Generate farewell messages with proper grammar - using the `inflect` library.

**File:** `ps4/adieu/adieu.py`

**Example:** Adieu, adieu, to Liesl, Friedrich, and Louisa

### Guessing Game
Number guessing game with levels - using the `random` module.

**File:** `ps4/game/game.py`

**Rules:**
- Prompt for level (positive integer)
- Generate random number between 1 and level
- Allow user to guess until correct

### Little Professor
Math quiz game - generating random arithmetic problems.

**File:** `ps4/professor/professor.py`

**Details:**
- Prompt for level (1, 2, or 3)
- Generate 10 problems
- Allow 3 attempts per problem
- Display final score

### Bitcoin Price Index
Get current Bitcoin price - using the `requests` library to call an API.

**File:** `ps4/bitcoin/bitcoin.py`

**Requirements:**
- Accept number of Bitcoins as command-line argument
- Fetch current USD price from API
- Calculate and display total value

## 🔍 Key Concepts

### Importing Modules
```python
# Import entire module
import random

# Import specific function
from random import choice

# Import with alias
import statistics as stats

# Import multiple items
from sys import argv, exit
```

### Random Module
```python
import random

# Random integer
num = random.randint(1, 10)

# Random choice from list
fruit = random.choice(["apple", "banana", "cherry"])

# Shuffle list
random.shuffle(my_list)
```

### Sys Module
```python
import sys

# Command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

filename = sys.argv[1]

# Exit with error
sys.exit(1)
```

### Requests Module
```python
import requests

# GET request
response = requests.get("https://api.example.com/data")

# Check status
if response.status_code == 200:
    data = response.json()
```

### Statistics Module
```python
import statistics

numbers = [1, 2, 3, 4, 5]
mean = statistics.mean(numbers)
median = statistics.median(numbers)
```

## 💡 Tips

1. **Read documentation** - Libraries have extensive docs
2. **Use pip** to install third-party packages: `pip install emoji`
3. **Check sys.argv** length before accessing arguments
4. **Handle API errors** with try-except
5. **Use aliases** for long module names
6. **Explore PyPI** - Python Package Index has thousands of libraries

## 📚 Additional Resources

- [Python Standard Library](https://docs.python.org/3/library/)
- [PyPI - Python Package Index](https://pypi.org/)
- [Requests Documentation](https://requests.readthedocs.io/)
- [Random Module](https://docs.python.org/3/library/random.html)

## 📦 Installing Packages

```bash
# Install a package
pip install emoji

# Install multiple packages
pip install requests pyfiglet inflect

# Install from requirements.txt
pip install -r requirements.txt

# List installed packages
pip list
```

## ▶️ Running the Code

```bash
# Navigate to a problem directory
cd week4/ps4/bitcoin

# Run with command-line argument
python bitcoin.py 2.5

# Figlet with font option
python figlet.py -f slant
python figlet.py --font rectangles
```

## 🎮 Example: Guessing Game Flow

```
Level: 5
Guess: 3
Too small!
Guess: 4
Just right!
```

## 🧪 Common Libraries

| Library | Purpose | Installation |
|---------|---------|--------------|
| `random` | Generate random numbers | Built-in |
| `statistics` | Statistical functions | Built-in |
| `sys` | System parameters | Built-in |
| `requests` | HTTP requests | `pip install requests` |
| `emoji` | Emoji support | `pip install emoji` |
| `pyfiglet` | ASCII art | `pip install pyfiglet` |
| `inflect` | Grammar engine | `pip install inflect` |

## 💻 Command-Line Arguments

```python
import sys

# Script name is sys.argv[0]
# Arguments start at sys.argv[1]

if len(sys.argv) != 2:
    sys.exit("Usage: python script.py <argument>")

arg = sys.argv[1]
```

---

[← Previous Week](../week3/README.md) | [Back to Main](../../README.md) | [Next Week →](../week5/README.md)
