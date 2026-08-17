
arr = [4,5,2,6,9,8,1,2,3]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i

        j = i+1
        while j< len(arr):
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1

        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr

print(selection_sort(arr))
