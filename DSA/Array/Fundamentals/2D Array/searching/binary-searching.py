arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

target = 5

rows = len(arr)
cols = len(arr[0])

i = 0
j = rows * cols - 1

while i <= j:
    mid = (i + j) // 2

    row = mid // cols
    col = mid % cols

    if arr[row][col] == target:
        print(row, col)
        break
    elif arr[row][col] < target:
        i = mid + 1
    else:
        j = mid - 1
else:
    print("Target not found")
