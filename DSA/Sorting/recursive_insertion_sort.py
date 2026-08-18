
arr =[5,2,8,4,1,6,7,3,9]
def insertion_sort(arr,count):
    if count >= len(arr):
        return arr
    key = arr[count]
    get_sorted(arr,count-1,key)
    insertion_sort(arr, count+1)
    return arr

def get_sorted(arr,count,key):
    if count>=0 and arr[count]>key:
        arr[count+1]=arr[count]
        count -=1
        get_sorted(arr,count,key)
    else:
        arr[count+1]= key
print(insertion_sort(arr,0))


