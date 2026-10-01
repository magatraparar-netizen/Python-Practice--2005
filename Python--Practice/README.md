# Python Practice

This repository contains my daily Python practice programs.

## Python Errors and Solutions

### 1. NameError: name 'length' is not defined

**Error:**

```text
NameError: name 'length' is not defined
```

**Reason:** The variables `length` and `width` were used before being properly defined or accessed.

**Solution:** Define the variables or access them using the correct object attributes.

**Correct Output:**

```text
20
```

### 2. Method Reference Instead of Method Call

**Output:**

```text
<bound method retangel.area of <__main__.retangel object>>
```

**Reason:** The method was printed without parentheses.

**Solution:**

```python
print(r.area())
```

### 3. IndentationError in Bike.py

**Error:**

```text
IndentationError: unindent does not match any outer indentation level
```

**Reason:** The indentation of `class bike(Vehicle):` did not match the surrounding code.

**Solution:** Align the class definition correctly and use consistent indentation (usually four spaces).

**Correct Output:**

```text
honda Start
```

## Learning Outcome

I learned how to identify and fix Python errors, call methods correctly, and use proper indentation.

