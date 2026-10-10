class Solution:
    def NnumbersSum(self, N):
        if N == 0:
            return 0
        return N + self.NnumbersSum(N - 1)
