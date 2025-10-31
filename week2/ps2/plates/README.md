# Vanity Plates - Week 2

## 🎯 Problem Description

In Massachusetts, home to Harvard University, it's possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

- "All vanity plates must start with at least two letters."
- "… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters."
- "Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a '0'."
- "No periods, spaces, or punctuation marks are allowed."

## 💻 Implementation

### `plates.py`

The main program that prompts the user for a vanity plate and validates it.

```python
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Implementation of validation logic
    ...
```

### `test_plates.py`

Unit tests to verify the validation logic works correctly for various cases.

## ✅ Validation Rules

1. **Length**: Between 2 and 6 characters
2. **Start**: Must begin with at least 2 letters
3. **Numbers**: Must come at the end (if present)
4. **First Number**: Cannot be '0'
5. **Characters**: Only alphanumeric (no spaces, periods, or punctuation)

## 📋 Examples

### Valid Plates
- `CS50` ✅
- `CS` ✅
- `HELLO` ✅
- `AB123` ✅

### Invalid Plates
- `C` ❌ (too short)
- `CS50P2` ❌ (too long)
- `50` ❌ (doesn't start with letters)
- `CS05` ❌ (first number is 0)
- `CS50P` ❌ (letter after number)
- `PI3.14` ❌ (contains punctuation)

## 🧪 Testing

Run the tests:

```bash
cd week2/ps2/plates
pytest test_plates.py -v
```

Run with coverage:

```bash
pytest test_plates.py --cov=plates --cov-report=term-missing
```

### Test Cases

The test suite covers:
- Minimum and maximum length validation
- Starting letter requirements
- Number placement rules
- First number cannot be zero
- Alphanumeric character validation
- Edge cases

## 🚀 Usage

```bash
python plates.py
```

**Example Session:**
```
Plate: CS50
Valid
```

```
Plate: CS05
Invalid
```

## 💡 Hints

1. Use string methods: `isalpha()`, `isdigit()`, `isalnum()`
2. Iterate through characters to find the first number
3. Check all conditions in a logical order
4. Handle edge cases (empty string, all letters, all numbers)

## 📚 Related Concepts

- String validation
- Character type checking
- Conditional logic
- Function design
- Unit testing with pytest

## 🔗 Resources

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [CS50P Week 2 - Loops](https://cs50.harvard.edu/python/2022/weeks/2/)

---

[← Back to Week 2](../README.md)
