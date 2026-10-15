class Solution:
    def countDigit(self, n):
        count = 0
        num = n
        while num != 0:
            num = num // 10
            count = count + 1
        return count

