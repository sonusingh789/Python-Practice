# 📁 File Handling in Python

This document explains various file handling techniques in Python, especially focusing on the use of **read mode (`r`)** and related operations.

---

## 📌 1. What is File Handling?

File handling allows us to:
- Create files
- Read data from files
- Write data into files
- Update existing files

Python provides built-in functions to handle files easily.

---

## 📖 2. File Opening Modes

| Mode | Description |
|------|------------|
| `r` | Read (default mode) |
| `w` | Write (overwrite file) |
| `a` | Append data |
| `r+` | Read + Write |
| `w+` | Write + Read |
| `a+` | Append + Read |

---

## 📘 3. Uses of `r` Mode (Read Mode)

`r` mode is used when we only want to **read data from a file**.

### ✔ Key Features:
- File must already exist
- Cannot modify file content
- Safe mode (no risk of overwriting data)

---

## 🧪 4. Reading Techniques in `r` Mode

### 🔹 1. read() → Read entire file
```python
with open("file.txt", "r") as file:
    content = file.read()
    print(content)