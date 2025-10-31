# Week 7 - Regular Expressions

## 📖 Overview

Week 7 introduces regular expressions (regex) - powerful patterns for matching and manipulating text. You'll learn how to use Python's `re` module to validate input, extract data, and search through text efficiently.

## 🎯 Learning Objectives

- Understand regular expression syntax
- Use the `re` module for pattern matching
- Validate input with regex patterns
- Extract specific data from text
- Use special characters and quantifiers
- Capture groups and backreferences
- Apply regex to real-world problems

## 📝 Problem Sets

### NUMB3RS
Validate IPv4 addresses using regular expressions.

**Files:**
- `ps7/numb3rs/numb3rs.py`
- `ps7/numb3rs/test_numb3rs.py`

**Requirements:**
- Accept IPv4 format: `#.#.#.#`
- Each number must be 0-255
- Return True/False for validity

### Watch on YouTube
Extract YouTube video IDs from URLs.

**File:** `ps7/watch/watch.py`

**Details:**
- Parse various YouTube URL formats
- Extract video ID
- Convert to embed URL format
- Handle http/https and www variations

### Working 9 to 5
Convert 12-hour time format to 24-hour format.

**File:** `ps7/working/working.py`

**Example:** `9:00 AM to 5:00 PM` → `09:00 to 17:00`

**Requirements:**
- Handle with/without minutes
- Validate time ranges
- Raise ValueError for invalid input

### Regular, um, Expressions
Count occurrences of "um" as a word (not as part of other words).

**Files:**
- `ps7/um/um.py`
- `ps7/um/test_um.py`

**Details:**
- Case-insensitive matching
- Match "um" as standalone word only
- Not in "yummy", "umbrella", etc.

### Response Validation
Validate email addresses using a library.

**File:** `ps7/response/response.py`

**Requirements:**
- Use `validator-collection` or similar
- Validate email format
- Return "Valid" or "Invalid"

## 🔍 Key Concepts

### Basic Patterns
```python
import re

# Simple match
if re.search("hello", text):
    print("Found!")

# Case-insensitive
if re.search("hello", text, re.IGNORECASE):
    print("Found!")

# Full string match
if re.fullmatch(r"\d+", text):
    print("All digits!")
```

### Special Characters
```
.    Any character except newline
\d   Digit (0-9)
\D   Non-digit
\w   Word character (a-z, A-Z, 0-9, _)
\W   Non-word character
\s   Whitespace
\S   Non-whitespace
^    Start of string
$    End of string
```

### Quantifiers
```
*     0 or more
+     1 or more
?     0 or 1
{n}   Exactly n times
{n,}  n or more times
{n,m} Between n and m times
```

### Character Classes
```python
[aeiou]     # Any vowel
[0-9]       # Any digit
[a-z]       # Lowercase letter
[A-Z]       # Uppercase letter
[^0-9]      # Not a digit
```

### Groups and Capturing
```python
# Capturing groups
match = re.search(r"(\d+)-(\d+)-(\d+)", "2023-10-31")
if match:
    year = match.group(1)   # "2023"
    month = match.group(2)  # "10"
    day = match.group(3)    # "31"

# Named groups
match = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})", "2023-10")
if match:
    print(match.group("year"))  # "2023"
```

### Common Patterns
```python
# Email (basic)
r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# URL
r"https?://[^\s]+"

# Phone number (US)
r"^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$"

# IPv4
r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
```

### re Module Functions
```python
import re

# Search anywhere in string
re.search(pattern, string)

# Match from beginning
re.match(pattern, string)

# Full string match
re.fullmatch(pattern, string)

# Find all matches
re.findall(pattern, string)

# Replace
re.sub(pattern, replacement, string)
```

## 💡 Tips

1. **Use raw strings** - `r"pattern"` to avoid escaping issues
2. **Test patterns** - Use regex101.com or pythex.org
3. **Be specific** - Narrow patterns prevent false matches
4. **Word boundaries** - Use `\b` for whole word matching
5. **Escape special chars** - Use `\` before `.`, `?`, `+`, etc.
6. **Start simple** - Build complex patterns incrementally
7. **Use groups** - Capture and extract specific parts

## 📚 Additional Resources

- [Python re Module](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
- [Regex101](https://regex101.com/) - Online regex tester
- [Pythex](https://pythex.org/) - Python regex tester

## ▶️ Running the Code

```bash
# NUMB3RS
cd week7/ps7/numb3rs
python numb3rs.py
pytest test_numb3rs.py -v

# Watch
cd week7/ps7/watch
python watch.py

# Um
cd week7/ps7/um
python um.py
pytest test_um.py -v
```

## 🧪 Testing Example: NUMB3RS

```python
# test_numb3rs.py
from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True

def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False

def test_format():
    assert validate("127.0.0") == False
    assert validate("127.0.0.1.1") == False
```

## 🎯 Pattern Examples

### IPv4 Validation
```python
import re

def validate(ip):
    # Pattern for IPv4
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    
    if match := re.search(pattern, ip):
        # Check each octet is 0-255
        for i in range(1, 5):
            if int(match.group(i)) > 255:
                return False
        return True
    return False
```

### YouTube URL Parsing
```python
import re

def parse(html):
    # Match various YouTube URL formats
    pattern = r'https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)'
    
    if match := re.search(pattern, html):
        return f"https://youtu.be/{match.group(1)}"
    return None
```

### Time Conversion
```python
import re

def convert(s):
    # Pattern: 9:00 AM to 5:00 PM or 9 AM to 5 PM
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    
    if match := re.search(pattern, s):
        # Extract and convert times
        # Implementation...
        pass
    else:
        raise ValueError
```

## 📖 Regex Cheat Sheet

| Pattern | Matches | Example |
|---------|---------|---------|
| `\d{3}` | Exactly 3 digits | `123` |
| `\w+` | One or more word chars | `hello` |
| `\s*` | Zero or more spaces | ` ` or `` |
| `[aeiou]` | Any vowel | `a`, `e` |
| `^hello` | Starts with "hello" | `hello world` |
| `world$` | Ends with "world" | `hello world` |
| `a.b` | a, any char, b | `a1b`, `axb` |
| `a|b` | a or b | `a` or `b` |
| `(abc)+` | One or more "abc" | `abc`, `abcabc` |

---

[← Previous Week](../week6/README.md) | [Back to Main](../../README.md) | [Next Week →](../week8/README.md)
