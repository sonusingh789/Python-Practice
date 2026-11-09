matrix = [[1, 2, 3], [4, 5, 6], [8, 9]]

m = len(matrix)
for i in range(m):
    n = len(matrix[i])
    for j in range(n):
        print(matrix[i][j], end="")
    print()
