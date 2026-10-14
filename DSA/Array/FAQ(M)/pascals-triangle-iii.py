class Solution:
    def pascalTriangleIII(self, n):

        result = []

        for i in range(1, n + 1):
            row = []
            res = 1

            for j in range(i):
                row.append(res)
                res = res * (i - 1 - j) // (j + 1)

            result.append(row)

        return result
