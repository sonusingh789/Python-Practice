arr = [2, 4, 6, 8, 10, 12]
k = 3

# brute force

for i in range(len(arr) - k + 1):
    sum = 0
    for j in range(i, i + k):
        sum += arr[j]
    print(sum, " ", end="")
