class Solution:
    def pascalTriangleII(self, r):

        result = []
        res = 1

        for i in range(r):
            result.append(res)
            res = res * (r - 1 - i) // (i + 1)
        return result
