###. Creating Hash Map
# ------------------------------

d = {}
d[1] = 100
d[2] = 200
d[3] = 300

# {1: 100, 2: 200, 3: 300}
# keys -> 1,2,3
# values -> 100,200,300

# ----------------------------
# OPERATIONS
# ---------------------------

# 1.  Insert or Update
d[4] = 400

# 2. Insert key : value if not present
d.setdefault(5, 500)

# 3. Get value through key get(k)
result = d.get(2)

# 4 . get value or defaut value
print(d.get(6, 0))  # 0

# 5 check if key is present
print(3 in d)  # returns true  or false.

# 6 check if value is present.
print(900 in d.values())  # True or false

# 7 Removing Key , dict.pop(key)
d.pop(1)

# 8  Returns all the keys in the dictionary
print(d.keys())
print(list(d.keys)) # returns keys as list.

# 9 return all the values as  a list.
print(list(d.values()))

# 10 return all  the key value pairs as a list of tuples.
print(list(d.items()))

# 11 size of HashMap/dict
print(len(d))

# 12 check if empty
print(not d) # false

# 13 clear()
d.clear()
