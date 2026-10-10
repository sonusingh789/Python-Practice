# 1 . creating Hash Map
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
