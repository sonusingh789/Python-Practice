arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]


def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linearSearch(arr, 200))
