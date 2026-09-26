class Solution:
    def largestDigit(self, n):
        largest = n%10

        while n!=0:
            num = n%10
            if num > largest:
                largest = num
            n = n//10

        return largest


