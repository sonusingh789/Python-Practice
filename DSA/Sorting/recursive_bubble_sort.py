arr  = [0,9,8,7,6,5,1,2,3,4]

def bubblePass(arr,count):
    if count >= len(arr)-1:
        return
    getSwap(arr,0,len(arr)-count-1)
    bubblePass(arr,count+1)
    return arr

def getSwap(arr,count,limit):
    if count >= limit:
        return
    if arr[count]>arr[count+1]:
        temp = arr[count]
        arr[count] = arr[count+1]
        arr[count+1] = temp
    getSwap(arr,count+1,limit)

print(bubblePass(arr,0))

