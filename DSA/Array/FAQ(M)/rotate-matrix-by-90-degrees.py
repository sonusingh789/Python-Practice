class Solution:
    def rotateMatrix(self, matrix):

        n = len(matrix)
        result = []
        # filling nxn result matrix with 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            result.append(row)

        for i in range(n):
            for j in range(n):
                result[j][n - 1 - i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]
