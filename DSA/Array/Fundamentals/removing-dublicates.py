arr = [1, 2, 3, 2, 3, 5, 4, 3, 6, 7, 3]

result = []

# method 1
for i in range(len(arr)):
    if arr[i] not in result:
        result.append(arr[i])
print(sorted(result))

# method 2
arr.sort()
visited = -1
for i in range(len(arr)):
    if arr[i] != visited:
        visited = arr[i]
        result.append(arr[i])
print(result)
