# Week 6 - File I/O

## 📖 Overview

Week 6 introduces file input/output (I/O) - reading from and writing to files. You'll learn how to work with text files, CSV files, and even manipulate images, making your programs capable of persistent data storage.

## 🎯 Learning Objectives

- Open, read, and write files
- Use context managers (`with` statement)
- Work with CSV files using the `csv` module
- Parse and manipulate structured data
- Handle file operations safely
- Work with PIL/Pillow for images
- Process command-line arguments for files

## 📝 Problem Sets

### Lines of Code
Count lines of code in a Python file, excluding comments and blank lines.

**File:** `ps6/lines/lines.py`

**Requirements:**
- Accept filename as command-line argument
- Validate `.py` file extension
- Exclude blank lines and comments
- Handle file not found errors

### Pizza Py
Create formatted tables from CSV data using `tabulate`.

**File:** `ps6/pizza/pizza.py`

**Details:**
- Read CSV file with menu data
- Format as ASCII table
- Handle command-line arguments
- Validate CSV file extension

### Scourgify
Clean and reorganize CSV data - splitting names into first and last.

**File:** `ps6/scourgify/scourgify.py`

**Requirements:**
- Read input CSV with "name,house" format
- Split "Last, First" into separate columns
- Write cleaned data to output CSV
- Expect two command-line arguments (input, output)

### CS50 P-Shirt
Overlay a shirt on a photo using PIL/Pillow.

**File:** `ps6/shirt/shirt.py`

**Details:**
- Accept two command-line arguments (input, output)
- Validate image extensions match
- Overlay CS50 shirt graphic
- Resize input to match shirt dimensions

## 🔍 Key Concepts

### Reading Files
```python
# Basic file reading
with open("file.txt") as file:
    contents = file.read()
    print(contents)

# Read line by line
with open("file.txt") as file:
    for line in file:
        print(line.rstrip())

# Read all lines into list
with open("file.txt") as file:
    lines = file.readlines()
```

### Writing Files
```python
# Write to file (overwrite)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")

# Append to file
with open("output.txt", "a") as file:
    file.write("New line\n")
```

### CSV Files
```python
import csv

# Reading CSV with DictReader
with open("data.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["house"])

# Writing CSV with DictWriter
with open("output.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerow({"first": "Harry", "last": "Potter", "house": "Gryffindor"})
```

### File Modes
```python
"r"  # Read (default)
"w"  # Write (overwrite)
"a"  # Append
"r+" # Read and write
"rb" # Read binary
"wb" # Write binary
```

### PIL/Pillow
```python
from PIL import Image, ImageOps

# Open image
image = Image.open("input.jpg")

# Resize
size = (600, 600)
image = ImageOps.fit(image, size)

# Paste overlay
shirt = Image.open("shirt.png")
image.paste(shirt, (0, 0), shirt)

# Save
image.save("output.jpg")
```

## 💡 Tips

1. **Always use `with`** - Automatically closes files
2. **Check file existence** before opening
3. **Validate extensions** for command-line arguments
4. **Use `rstrip()`** to remove newlines when reading
5. **DictReader/DictWriter** for CSV with headers
6. **Handle exceptions** - FileNotFoundError, etc.
7. **Binary mode** for images and non-text files

## 📚 Additional Resources

- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [CSV Module](https://docs.python.org/3/library/csv.html)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Working with Files](https://realpython.com/working-with-files-in-python/)

## 📦 Installing Packages

```bash
# Install Pillow for image manipulation
pip install Pillow

# Install tabulate for table formatting
pip install tabulate
```

## ▶️ Running the Code

```bash
# Lines of Code
cd week6/ps6/lines
python lines.py hello.py

# Pizza Py
cd week6/ps6/pizza
python pizza.py sicilian.csv

# Scourgify
cd week6/ps6/scourgify
python scourgify.py before.csv after.csv

# Shirt
cd week6/ps6/shirt
python shirt.py before.jpg after.jpg
```

## 🧪 Error Handling Example

```python
import sys

# Check argument count
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check file extension
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

# Check file exists
try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")
```

## 📋 CSV Processing Pattern

```python
import csv
import sys

# Read input CSV
students = []
with open("input.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "first": row["first"],
            "last": row["last"],
            "house": row["house"]
        })

# Write output CSV
with open("output.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        writer.writerow(student)
```

## 🎨 Image Processing Pattern

```python
from PIL import Image, ImageOps
import sys

# Validate arguments and extensions
if len(sys.argv) != 3:
    sys.exit("Usage: python program.py input output")

input_ext = sys.argv[1].split(".")[-1].lower()
output_ext = sys.argv[2].split(".")[-1].lower()

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

# Open and process image
try:
    image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    
    # Resize to match shirt
    size = shirt.size
    image = ImageOps.fit(image, size)
    
    # Overlay shirt
    image.paste(shirt, (0, 0), shirt)
    
    # Save result
    image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
```

---

[← Previous Week](../week5/README.md) | [Back to Main](../../README.md) | [Next Week →](../week7/README.md)
