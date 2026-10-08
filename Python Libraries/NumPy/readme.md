# NumPy

> Python's fundamental package for scientific computing.

NumPy is Python's fundamental package for scientific computing. Its core is the **ndarray**, a multi-dimensional array object, along with fast routines for mathematical operations, sorting, selecting, I/O, linear algebra, statistics, and random simulations.

---

## 📚 Table of Contents

1. [What is NumPy?](#what-is-numpy)
2. [Creating Arrays](#1-creating-arrays)
3. [Array Attributes](#2-array-attributes)
4. [Changing Data Types - astype](#3-changing-data-types---astype)
5. [Array Operations](#4-array-operations)
6. [Mathematical Functions](#5-mathematical-functions)
7. [Indexing and Slicing](#6-indexing-and-slicing)
8. [Iterating Over Arrays](#7-iterating-over-arrays)
9. [Reshaping & Stacking](#8-reshaping--stacking)
10. [Splitting Arrays](#9-splitting-arrays)
11. [Advanced Indexing & Masking](#10-advanced-indexing--masking)
12. [Mathematical Formulas](#11-mathematical-formulas)
13. [Handling Missing Values](#12-handling-missing-values)
14. [Plotting Graphs](#13-plotting-graphs)
15. [Sorting & Adding Elements](#14-sorting--adding-elements)
16. [Finding & Filtering](#15-finding--filtering)

---

# What is NumPy?

**NumPy** stands for **Numerical Python**.

It provides:

- `ndarray` — multi-dimensional arrays
- Fast numerical operations
- Mathematical functions
- Statistical functions
- Linear algebra operations
- Array manipulation
- Sorting and searching
- Random number generation
- Support for scientific and machine learning workflows

### Why NumPy?

Python lists are flexible but can become slow when working with large amounts of numerical data.

NumPy arrays are designed for efficient numerical computation.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)