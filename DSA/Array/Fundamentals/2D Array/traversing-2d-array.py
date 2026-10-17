arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# from  right to left
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

# buttom to right
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[j][i], end=" ")
    print()


