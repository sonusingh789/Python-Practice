s = {10, 20, 30}

s.add(40)
s.remove(20)
s.discard(99)  # safely remove , no error if absent.

print(10 in s)  # contains check

# add all element
s.update([60, 40, 30])

# remove matching element.
s.difference_update({10, 50})

# keep only matching elements.
s.intersection_update({30, 60, 70})

# size
len(s)

# check is empty
print(not s)

# clear
s.clear()


# ---------------------
# SET OPERATIONS
# ----------------------

S1 = {1, 2, 3, 4}
S2 = {3, 4, 5, 6}

# UNION - elements from both set
print(S1 | S2)

# INTERSECTION - Common Element
print(S1 & S2)

# DIFFERENCE - Element in S1 but Not in S2
print(S1 - S2)

# Symmetric difference — elements in either, but not both
print(S1 ^ S2)

# -------------------------------
#  LinkedHashSet - preserves Insertion Order.
# -------------------------------

lst = [30, 10, 20, 10, 30]
s = dict.fromkeys(lst)
print(list(s))

d = dict.fromkeys([30, 10, 20])
d.setdefault(40, None)
d.setdefault(10, None)
print(list(d))

# ----------------------------------
#  Tree Set - unique elements in sorted order
# -------------------------------

lst = [40, 10, 30, 10, 20, 30]
s = sorted(set(lst))
print(s)
