arr = [1, 2, 0, 3, 4, 0, 0, 5, 6, 0, 7, 8, 9]

j = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[j] = arr[i]
        j += 1

while j < len(arr):
    arr[j] = 0
    j += 1

print(arr)
