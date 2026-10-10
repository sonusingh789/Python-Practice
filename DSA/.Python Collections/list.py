my_list: list[int] = [1, 2, 3, 5, 6]

# 1. append(x) — Add an element to the end
my_list.append(5)
my_list.append(6)

# 2. insert(i, x) — Insert an element at index i
my_list.insert(1, 15)

# 3. extend(iterable) — Add all elements from another iterable
my_list.extend([1, 3, 4])

# 4. Access an element using index
x = my_list[0]

# 5. Update an element at index i
my_list[0] = 5

# 6. pop(i) — Remove and return the element at index i
x = my_list.pop(2)
my_list.pop()  # removes last element.

# 7. remove(x) — Remove the first occurrence of a value
my_list.remove(5)

# 8. Check whether an element exists
result = 5 in my_list  # Returns True or False

# 9. index(x) — Find the first index of a value
result = my_list.index(5)  # Raises ValueError if not found

# 10. len(list) — Get the number of elements
size = len(my_list)

# 11. clear() — Remove all elements
my_list.clear()

# 12 . Reverse List
my_list.reverse()

# 13 copy a list
new_copied_list = my_list.copy()

# 14 count frequency
freq = my_list.count(10)


# -------------------------
## SORTING
# -------------------------

lst = [40, 10, 30, 20]

# 1 . Sort ORIGINAL list
lst.sort()
# 2 .Sort in descending order
lst.sort(reverse=True)
# 3 .Create a new sorted list without modifying the original.
lst = [40, 10, 30, 20]
new_lst = sorted(lst)

# --------------------------------
#  SEARCHING - alt Binary Search
# --------------------------------


from bisect import bisect_left

lst = [10, 20, 30, 40, 50, 60]
x = 30

i = bisect_left(lst, x)

if i < len(lst) and lst[i] == x:
    print(i)
else:
    print(-1)


# Useful methods

# 1.  minimum / maximum  value in a list.
print(min(my_list), max(my_list))

# 2 . sum of elements
print(sum(my_list))
# 3 . first and last element
print(my_list[0], my_list[-1])
