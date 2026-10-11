arr = [56, 34, 22, 4, 5, 37, 45, 66, 45, 33]

arr.sort()


def binarySearch(arr, data):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == data:
            return mid
        elif arr[mid] < data:
            l = mid + 1
        else:
            r = mid - 1
    return -1


print(binarySearch(arr, 37))
