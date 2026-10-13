arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = []

# First row: left to right
for i in range(len(arr[0])):
    result.append(arr[0][i])

# Last column: top to bottom
for i in range(1, len(arr)):
    result.append(arr[i][2])

# Last row: right to left
for i in range(len(arr[2]) - 2, -1, -1):
    result.append(arr[2][i])

# First column: bottom to top
for i in range(len(arr) - 2, 0, -1):
    result.append(arr[i][0])

# Center element
result.append(arr[1][1])
