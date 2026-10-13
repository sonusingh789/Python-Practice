arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def linear_search(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == target:
                return i, j
    return -1, -1


print(linear_search(arr, 7))
