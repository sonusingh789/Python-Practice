arr = [1, 2, 3, 4, 1]

# brute force
# contains = False
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == arr[j]:
#             contains = True
# print(contains)


# using two pointers.

arr.sort()

i = 0
j = 1
contains = False
while j < len(arr):
    if arr[i] == arr[j]:
        contains = True
        break
    else:
        i += 1
        j += 1
print(contains)
