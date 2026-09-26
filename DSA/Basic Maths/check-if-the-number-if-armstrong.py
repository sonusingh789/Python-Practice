class Solution:
    def isArmstrong(self, n):
        arm = 0
        count = 0
        num = n
        original = n

        while num != 0:
            num = num // 10
            count += 1

        while n != 0:
            digit = n % 10
            arm += digit ** count
            n = n // 10

        return original == arm