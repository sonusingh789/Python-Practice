arr = [1,2,4,5,2,45,4,34,5,56,57,4,2]
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr
print(bubble_sort(arr))
