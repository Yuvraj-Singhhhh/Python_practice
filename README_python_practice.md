# Python Basics – Day 1 & Day 2

A beginner-friendly collection of Python practice programs covering the fundamentals of Python syntax, variables, data types, operators, strings, lists, user input, and basic built-in functions.

## 📚 Contents

- [About](#about)
- [Topics Covered](#topics-covered)
- [Files](#files)
- [Getting Started](#getting-started)
- [Examples](#examples)
- [Learning Progress](#learning-progress)
- [Next Steps](#next-steps)

## About

This repository contains hands-on Python exercises created while learning Python from the ground up.

The examples focus on understanding concepts by writing and running small programs rather than relying only on theory.

The current lessons introduce basic concepts such as variables, dynamic typing, numeric operations, collections, string manipulation, user input, and Boolean logic.

## Topics Covered

### Day 1

- Variables and `print()`
- Python dynamic typing
- Basic data types:
  - `int`
  - `str`
  - `float`
  - `bool`
  - `None`
- Collections:
  - Lists
  - Tuples
  - Sets
  - Dictionaries
- Arithmetic operations
- The `math` module
- User input with `input()`
- Type conversion with `int()`
- f-strings
- Escape sequences
- Multi-line strings
- String replacement and formatting
- String indexing and slicing
- `strip()`, `lstrip()`, and `rstrip()`
- Case-insensitive string comparison
- `startswith()` and `endswith()`
- `find()` and the `in` operator
- String validation with `isalpha()` and `isnumeric()`
- `join()`
- `zfill()`

The Day 1 exercises include examples of string indexing, whitespace cleanup, validation, and formatting. fileciteturn0file0L94-L155

### Day 2

- Checking data types with `type()`
- Numeric data types:
  - Integers
  - Floats
  - Complex numbers
- Arithmetic operators
- Comparison operators
- Logical operators:
  - `and`
  - `or`
  - `not`
- `math.ceil()`
- `math.floor()`
- `round()`
- Lists
- `append()`
- `pop()`
- `len()`
- Membership testing with `in`
- Basic `if/else` statements

The Day 2 exercises also demonstrate arithmetic, comparisons, Boolean logic, and basic list operations. fileciteturn0file1L21-L69

## Files

| File | Description |
| --- | --- |
| `day_1.py` | Python fundamentals, strings, input, formatting, and basic data structures |
| `day_2.py` | Numeric types, operators, Boolean logic, lists, and membership testing |

## Getting Started

### 1. Install Python

Download and install Python 3 from the official Python website.

### 2. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 3. Run an exercise

```bash
python day_1.py
```

or:

```bash
python day_2.py
```

Depending on your system, you may need to use:

```bash
python3 day_1.py
```

## Examples

### Variables

```python
name = "Yuvraj"
print(name)
```

### Arithmetic

```python
x = 10
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
```

### User Input

```python
name = input("Enter your name: ")
print("Hello", name)
```

### String Methods

```python
email = "example@gmail.com"

print(email.find("@"))
print("@" in email)
print(email.endswith(".com"))
```

### Lists

```python
names = ["yuvraj", "rishi", "mihir"]

names.append("yuko")
print(names)

names.pop(1)
print(names)
```

## Learning Progress

This project is intended to grow as Python learning continues.

Current progression:

```text
Python Basics
     │
     ├── Variables & Data Types
     ├── Operators
     ├── User Input
     ├── Strings
     ├── Lists & Collections
     ├── Boolean Logic
     └── Built-in Functions
```

## Next Steps

Possible topics to add in future lessons:

- Conditional statements in more depth
- `for` and `while` loops
- Functions
- Dictionaries and sets in depth
- List comprehensions
- Exception handling
- File handling
- Modules and packages
- Object-oriented programming
- NumPy and Pandas
- Data analysis and data engineering fundamentals

## Notes

These files are learning exercises, so some examples are intentionally simple and may contain experiments or comments written during practice. The goal is to understand the concepts progressively and improve the code as learning continues.

---

**Status:** 🚧 Learning in progress

**Language:** Python 3

**Level:** Beginner
