matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in range(len(matrix[0])):
    for col in range(len(matrix[row])):
        print(matrix[col][row], end="")
    print()
