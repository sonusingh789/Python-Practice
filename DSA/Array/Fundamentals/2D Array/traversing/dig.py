mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

col = 0
for row in range(len(mat)):
    print(mat[row][col])
    col += 1

c = len(mat) - 1
for r in range(len(mat)):
    size = len(mat) - 1
    if r == c:
        c -= 1
        continue
    else:
        print(mat[r][c])
        c -= 1
