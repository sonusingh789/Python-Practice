arr = [1,3,3,5,6,4,67,3,9,7,9]
def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1]=key
    return arr
print(insertion_sort(arr))
