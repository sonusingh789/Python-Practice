class Solution:
    def pascalTriangleI(self, r, c):
        res = 1

        n = r - 1
        k = c - 1

        for i in range(k):
            res = res * (n - i)
            res = res // (i + 1)

        return res
