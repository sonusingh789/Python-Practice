hashmap = {}

nums = [1, 2, 3, 4, 5]


# dict[key] → gets the value.
# for key in dict: → gets keys one by one.
# dict.keys() → gets all keys.
# for key in dict:
# print(key one by one )
# for key , vale  in dict.items():
# print(key , value)
# freq.get(key, 0) → return the value if the key exists; otherwise return 0.
# adding element

# adding
for i in range(len(nums)):
    hashmap[i] = nums[i]
print()

# getting key
for key in hashmap:
    print(key, end=" ")
print()

# getting value
for i in range(len(hashmap)):
    print(hashmap[i], end=" ")
print()

for i in range(len(hashmap)):
    x = hashmap.get(i, -1)
    print(x, end=" ")
