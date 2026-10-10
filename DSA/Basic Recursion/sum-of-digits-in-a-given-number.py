class Solution:
    def addDigits(self, num, sum=0):
        if num == 0:
            if sum < 10:
                return sum
            return self.addDigits(sum, 0)

        return self.addDigits(num // 10, sum + num % 10)
