# Week 8 - Object-Oriented Programming

## 📖 Overview

Week 8 introduces Object-Oriented Programming (OOP) - a paradigm for structuring code using classes and objects. You'll learn how to create custom types, encapsulate data and behavior, and build more organized, reusable programs.

## 🎯 Learning Objectives

- Understand classes and objects
- Create custom classes with attributes and methods
- Use `__init__` for initialization
- Implement class methods and properties
- Use decorators like `@property` and `@classmethod`
- Understand inheritance and composition
- Apply OOP principles to real problems
- Work with operator overloading

## 📝 Problem Sets

### Seasons of Love
Calculate age in minutes using object-oriented approach.

**File:** `ps8/seasons/seasons.py`

**Requirements:**
- Accept birth date as input (YYYY-MM-DD)
- Calculate minutes lived
- Display in words (using `inflect`)
- Use classes and methods

### Cookie Jar
Implement a cookie jar class with deposit and withdraw methods.

**Files:**
- `ps8/jar/jar.py`
- `ps8/jar/test_jar.py`

**Details:**
- Track cookie capacity
- Deposit cookies (up to capacity)
- Withdraw cookies (not more than available)
- Raise `ValueError` for invalid operations
- Implement `__str__` for display

### CS50 Shirtificate
Generate a PDF certificate with custom name.

**File:** `ps8/shirtificate/shirtificate.py`

**Requirements:**
- Use `fpdf` library
- Create PDF with CS50 shirt image
- Overlay user's name on shirt
- Save as `shirtificate.pdf`

## 🔍 Key Concepts

### Classes and Objects
```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

# Create objects
harry = Student("Harry", "Gryffindor")
print(harry)  # Harry from Gryffindor
```

### Properties and Validation
```python
class Student:
    def __init__(self, name, house):
        self.name = name  # Uses setter
        self.house = house
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
```

### Class Methods
```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

# Use class method
student = Student.get()
```

### Operator Overloading
```python
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
```

### Inheritance
```python
class Wizard:
    def __init__(self, name):
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
```

## 💡 Tips

1. **Use `@property`** for attribute validation
2. **Private attributes** - Prefix with `_` by convention
3. **`__init__`** - Initialize object state
4. **`__str__`** - Define string representation
5. **Class methods** - Use `@classmethod` for alternate constructors
6. **Keep classes focused** - Single responsibility principle
7. **Raise exceptions** for invalid states

## 📚 Additional Resources

- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Properties and Decorators](https://docs.python.org/3/library/functions.html#property)
- [FPDF Documentation](https://pyfpdf.readthedocs.io/)

## 📦 Installing Packages

```bash
# Install fpdf for PDF generation
pip install fpdf2

# Install inflect for number to words
pip install inflect
```

## ▶️ Running the Code

```bash
# Seasons
cd week8/ps8/seasons
python seasons.py

# Cookie Jar
cd week8/ps8/jar
python jar.py
pytest test_jar.py -v

# Shirtificate
cd week8/ps8/shirtificate
python shirtificate.py
```

## 🧪 Testing Example: Cookie Jar

```python
# test_jar.py
from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(5)
    assert jar.capacity == 5

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    
def test_deposit_overflow():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5

def test_withdraw_underflow():
    jar = Jar(10)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(5)

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
```

## 🎯 Cookie Jar Implementation

```python
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
```

## 📖 Common Magic Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `__init__` | Constructor | `obj = MyClass()` |
| `__str__` | String representation | `str(obj)`, `print(obj)` |
| `__repr__` | Official representation | `repr(obj)` |
| `__add__` | Addition operator | `obj1 + obj2` |
| `__eq__` | Equality operator | `obj1 == obj2` |
| `__len__` | Length | `len(obj)` |
| `__getitem__` | Indexing | `obj[key]` |
| `__setitem__` | Assignment | `obj[key] = value` |

## 💻 PDF Generation Example

```python
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", align="C")

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", size=24)
pdf.image("shirtificate.png", x=0, y=70, w=pdf.epw)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 250, "Your Name", align="C")
pdf.output("shirtificate.pdf")
```

## 🎓 OOP Principles

### Encapsulation
Bundle data and methods that work on that data within a class.

### Abstraction
Hide complex implementation details, expose simple interfaces.

### Inheritance
Create new classes based on existing classes.

### Polymorphism
Objects of different types can be treated uniformly.

## 🔧 Design Patterns

### Constructor Pattern
```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```

### Factory Pattern
```python
class Student:
    @classmethod
    def from_input(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
```

### Property Pattern
```python
class Student:
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
```

---

[← Previous Week](../week7/README.md) | [Back to Main](../../README.md) | [Next Week →](../week9/README.md)
