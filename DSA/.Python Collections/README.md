# 🐍 Python Collections 


## Table of Contents

| # | Collection | File | One-line purpose |
|---|------------|------|------------------|
| 1 | [List](#1-list) | `list.py` | Ordered, indexed, mutable sequence |
| 2 | [Dictionary (HashMap)](#2-dictionary-hashmap) | `dict_hashmap.py` | Key → value mapping with fast lookup |
| 3 | [Set (HashSet)](#3-set-hashset) | `set_hashset.py` | Unique values with fast membership tests |
| 4 | [Stack](#4-stack) | `stack.py` | LIFO — last in, first out |
| 5 | [Queue (deque)](#5-queue-deque) | `queue.py` | FIFO — first in, first out |
| 6 | [Heap (heapq)](#6-heap-heapq) | `heapq.py` | Priority queue — smallest item always first |

---

##  Cheat Sheet:

| I need to... | Use |
|--------------|-----|
| Keep items in order and access them by index | `list` |
| Look up a value by a key (name, id) | `dict` |
| Remove duplicates or check "have I seen this?" | `set` |
| Undo, backtrack, or match brackets | stack (`list`) |
| Process items in arrival order (BFS, scheduling) | queue (`deque`) |
| Always get the smallest (or largest) item next | heap (`heapq`) |

##  Time Complexity at a Glance

| Structure | Operation | Average cost |
|-----------|-----------|--------------|
| List | `append()`, `pop()` (end), index access | O(1) |
| List | `insert(i, x)`, `pop(i)`, `remove(x)`, `index(x)`, `x in list` | O(n) |
| List | `sort()` | O(n log n) |
| Dict | get / insert / delete / `key in d` | O(1) |
| Set | `add`, `remove`, `discard`, `x in s` | O(1) |
| Stack (list) | `append()`, `pop()`, `st[-1]` | O(1) |
| Queue (deque) | `append`, `appendleft`, `pop`, `popleft` | O(1) |
| Heap | `heappush`, `heappop` | O(log n) |
| Heap | peek `h[0]` | O(1) |

---

## 1. List

**Purpose:** An ordered, indexed, mutable collection that allows duplicates.

**Properties**

- Ordered and indexed (starts at `0`, negative indexes count from the end)
- Allows duplicate values
- Mutable: can change after creation
- Great for sequential data

### Common operations 

| Operation | Description | Example |
|-----------|-------------|---------|
| `append(x)` | Add an element to the end | `[1, 2].append(3)` → `[1, 2, 3]` |
| `insert(i, x)` | Insert an element at index `i` | `[1, 3].insert(1, 2)` → `[1, 2, 3]` |
| `extend(iterable)` | Add all elements from another iterable | `[1, 2].extend([3, 4])` → `[1, 2, 3, 4]` |
| `lst[i]` | Access an element by index | `[10, 20, 30][0]` → `10` |
| `lst[i] = x` | Update the element at index `i` | `lst[0] = 5` → `[5, 20, 30]` |
| `pop(i)` | Remove and return the element at index `i` (last if omitted) | `[10, 20, 30].pop(1)` → returns `20` |
| `remove(x)` | Remove the first occurrence of a value | `[5, 6, 5].remove(5)` → `[6, 5]` |
| `x in lst` | Check whether an element exists | `5 in [5, 6]` → `True` |
| `index(x)` | First index of a value (raises `ValueError` if missing) | `[5, 6, 7].index(6)` → `1` |
| `len(lst)` | Number of elements | `len([1, 2, 3])` → `3` |
| `count(x)` | Frequency of a value | `[1, 2, 1, 1].count(1)` → `3` |
| `reverse()` | Reverse the list in place | `[1, 2, 3].reverse()` → `[3, 2, 1]` |
| `copy()` | Shallow copy of the list | `b = a.copy()` → `b` is a separate list |
| `clear()` | Remove all elements | `[1, 2].clear()` → `[]` |

### example

```python
numbers = [10, 20, 30]
numbers.append(40)       # [10, 20, 30, 40]
numbers.insert(1, 15)    # [10, 15, 20, 30, 40]
numbers.pop()            # removes 40
numbers.sort()           # [10, 15, 20, 30]
```

### Sorting

| Operation | Description | Example |
|-----------|-------------|---------|
| `sort()` | Sort the original list (ascending) | `[40, 10, 30].sort()` → `[10, 30, 40]` |
| `sort(reverse=True)` | Sort the original list (descending) | `[40, 10, 30].sort(reverse=True)` → `[40, 30, 10]` |
| `sorted(lst)` | Return a new sorted list, original unchanged | `sorted([40, 10, 30])` → `[10, 30, 40]` |

### Binary search (on a sorted list)

```python
from bisect import bisect_left

lst = [10, 20, 30, 40, 50, 60]
x = 30

i = bisect_left(lst, x)
print(i if i < len(lst) and lst[i] == x else -1)   # 2
```

### built-ins

| Built-in | Description | Example |
|----------|-------------|---------|
| `min(lst)`, `max(lst)` | Smallest / largest value | `min([3, 1, 2])` → `1` |
| `sum(lst)` | Sum of elements | `sum([1, 2, 3])` → `6` |
| `lst[0]`, `lst[-1]` | First and last element | `[7, 8, 9][-1]` → `9` |

**Use**

- You need ordered data
- You want to access items by position
- You want to maintain a sequence

---

## 2. Dictionary (HashMap)

**Purpose:** Stores data as **key → value** pairs for fast lookup by key.

**Properties**

- Keys must be unique (and hashable); values can repeat
- Insertion-ordered in Python 3.7+ (unordered in older versions)
- Average O(1) lookup, insert, and delete

### Common operations (with examples)

Assume `d = {1: 100, 2: 200}` unless stated otherwise.

| Operation | Description | Example |
|-----------|-------------|---------|
| `d[key] = value` | Insert or update | `d[3] = 300` → `{1: 100, 2: 200, 3: 300}` |
| `d.get(key)` | Get value (returns `None` if missing) | `d.get(2)` → `200` |
| `d.get(key, default)` | Get value with a fallback | `d.get(9, 0)` → `0` |
| `d.setdefault(key, value)` | Insert only if the key is missing | `d.setdefault(5, 500)` → adds `5: 500` |
| `key in d` | Check if a key exists | `1 in d` → `True` |
| `value in d.values()` | Check if a value exists (O(n)) | `900 in d.values()` → `False` |
| `d.pop(key)` | Remove a key and return its value | `d.pop(1)` → returns `100` |
| `d.keys()` | All keys | `list(d.keys())` → `[1, 2]` |
| `d.values()` | All values | `list(d.values())` → `[100, 200]` |
| `d.items()` | All `(key, value)` pairs | `list(d.items())` → `[(1, 100), (2, 200)]` |
| `len(d)` | Number of pairs | `len(d)` → `2` |
| `not d` | `True` if empty | `not {}` → `True` |
| `d.clear()` | Remove everything | `d.clear()` → `{}` |

### example

```python
student = {1: "Alice", 2: "Bob"}
student[3] = "Charlie"        # insert
name = student.get(2)         # "Bob"
print(student.get(9, "N/A"))  # "N/A" (fallback)
print(list(student.keys()))   # [1, 2, 3]
print(list(student.items()))  # [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
```

> 💡 `d.keys()` is a method call. Use `list(d.keys())`, not `list(d.keys)`.

**Use**

- You need fast lookup by name or id
- You want to store related data together
- You need a mapping like `name → value` (also great for frequency counting)

---

## 3. Set (HashSet)

**Purpose:** Stores **unique** values only, with fast membership checks and math-style set operations.

**Properties**

- Unordered, no indexing
- No duplicates
- Average O(1) membership test
- Elements must be hashable

### Common operations 

Assume `s = {10, 20, 30}` unless stated otherwise.

| Operation | Description | Example |
|-----------|-------------|---------|
| `add(x)` | Add an element | `s.add(40)` → `{10, 20, 30, 40}` |
| `remove(x)` | Remove an element (raises `KeyError` if absent) | `s.remove(20)` → `{10, 30}` |
| `discard(x)` | Remove an element safely (no error if absent) | `s.discard(99)` → no change, no error |
| `update(iterable)` | Add all elements from an iterable | `s.update([60, 40])` → `{10, 20, 30, 40, 60}` |
| `difference_update(other)` | Remove elements that appear in `other` | `s.difference_update({10, 50})` → `{20, 30}` |
| `intersection_update(other)` | Keep only elements that appear in `other` | `s.intersection_update({30, 60})` → `{30}` |
| `x in s` | Membership check | `10 in s` → `True` |
| `len(s)` | Number of elements | `len(s)` → `3` |
| `not s` | `True` if empty | `not set()` → `True` |
| `clear()` | Remove everything | `s.clear()` → `set()` |

### example

```python
s = {10, 20, 30}
s.add(40)
s.discard(99)       # safe, no error
print(20 in s)      # True
```

### Set operations

Assume `S1 = {1, 2, 3, 4}` and `S2 = {3, 4, 5, 6}`.

| Operator | Name | Description | Example result |
|----------|------|-------------|----------------|
| `S1 \| S2` | Union | Elements from both sets | `{1, 2, 3, 4, 5, 6}` |
| `S1 & S2` | Intersection | Common elements | `{3, 4}` |
| `S1 - S2` | Difference | In `S1` but not in `S2` | `{1, 2}` |
| `S1 ^ S2` | Symmetric difference | In either, but not both | `{1, 2, 5, 6}` |

### patterns

| Goal | Example | Result |
|------|---------|--------|
| Remove duplicates, keep insertion order | `list(dict.fromkeys([30, 10, 20, 10, 30]))` | `[30, 10, 20]` |
| Remove duplicates, sorted output | `sorted(set([40, 10, 30, 10, 20, 30]))` | `[10, 20, 30, 40]` |

**Use**

- You want unique values
- You need fast membership testing
- You need set math (union, intersection, difference)

---

## 4. Stack

**Purpose:** **LIFO** (Last In, First Out). The last item inserted is the first one removed.

Think of a stack of plates: you add and remove from the top.

### Operations

Assume `st = [10, 20, 30]` (top is `30`) unless stated otherwise.

| Operation | Code | Description | Example |
|-----------|------|-------------|---------|
| Push | `st.append(x)` | Add to the top | `st.append(40)` → `[10, 20, 30, 40]` |
| Pop | `st.pop()` | Remove and return the top item | `st.pop()` → returns `30` |
| Peek | `st[-1]` | Look at the top without removing | `st[-1]` → `30` |
| Is empty | `not st` | `True` if empty | `not []` → `True` |
| Size | `len(st)` | Number of items | `len(st)` → `3` |
| Clear | `st.clear()` | Remove everything | `st.clear()` → `[]` |

###  example

```python
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack[-1])   # 30 (peek)
stack.pop()        # removes 30
```

**Use**

- Undo / redo
- Backtracking
- Expression evaluation and bracket matching
- Recursion-related logic (simulating the call stack)

---

## 5. Queue (deque)

**Purpose:** **FIFO** (First In, First Out). The first item inserted is the first one removed.

Think of a line at a ticket counter. Use `collections.deque` instead of a list, because `list.pop(0)` is O(n) while `deque.popleft()` is O(1).

### Operations 

Assume `from collections import deque` and `dq = deque([10, 20, 30])` unless stated otherwise.

| Operation | Code | Description | Example |
|-----------|------|-------------|---------|
| Enqueue (right) | `dq.append(x)` | Add to the back | `dq.append(40)` → `deque([10, 20, 30, 40])` |
| Add to left | `dq.appendleft(x)` | Add to the front | `dq.appendleft(5)` → `deque([5, 10, 20, 30])` |
| Dequeue (front) | `dq.popleft()` | Remove from the front | `dq.popleft()` → returns `10` |
| Remove from back | `dq.pop()` | Remove from the back | `dq.pop()` → returns `30` |
| Front | `dq[0]` | First element | `dq[0]` → `10` |
| Back | `dq[-1]` | Last element | `dq[-1]` → `30` |
| Is empty | `not dq` | `True` if empty | `not deque()` → `True` |
| Size | `len(dq)` | Number of items | `len(dq)` → `3` |

### example

```python
from collections import deque

q = deque()
q.append(10)
q.append(20)
q.appendleft(5)    # deque([5, 10, 20])
q.popleft()        # removes 5
```

> A `deque` is double-ended, so it works as both a queue and a stack.

**Use**

- Task scheduling
- BFS (breadth-first search) traversal
- Processing requests in arrival order

---

## 6. Heap (heapq)

**Purpose:** A **priority queue** where the **smallest element is always at the front** (min-heap).

**Properties**

- Built on top of a plain list
- `h[0]` is always the smallest item
- The rest of the list is only partially ordered, so don't expect a fully sorted print

### Operations 

Assume `import heapq` and `h = [10, 30, 20]` (already a valid heap) unless stated otherwise.

| Operation | Code | Description | Example |
|-----------|------|-------------|---------|
| Push | `heapq.heappush(h, x)` | Insert an element (O(log n)) | `heapq.heappush(h, 5)` → `5` is now at `h[0]` |
| Pop | `heapq.heappop(h)` | Remove and return the smallest (O(log n)) | `heapq.heappop(h)` → returns `10` |
| Peek | `h[0]` | View the smallest (O(1)) | `h[0]` → `10` |
| Size | `len(h)` | Number of items | `len(h)` → `3` |
| Is empty | `not h` | `True` if empty | `not []` → `True` |
| Clear | `h.clear()` | Remove everything | `h.clear()` → `[]` |

###  example (min-heap)

```python
import heapq

h = []
heapq.heappush(h, 30)
heapq.heappush(h, 10)
heapq.heappush(h, 20)

print(h)                 # [10, 30, 20]  (heap order, not sorted)
print(h[0])              # 10
print(heapq.heappop(h))  # 10
```

### Max-heap trick

`heapq` only provides a min-heap, so store **negative values** to simulate a max-heap.

```python
h = []
heapq.heappush(h, -10)
heapq.heappush(h, -30)
heapq.heappush(h, -20)

print(-h[0])              # 30 (peek max)
print(-heapq.heappop(h))  # 30
print(-heapq.heappop(h))  # 20
print(-heapq.heappop(h))  # 10
```

**Use**

- Finding the smallest or largest elements efficiently
- Priority scheduling
- Merging K sorted lists
- Dijkstra and other shortest-path algorithms

---


