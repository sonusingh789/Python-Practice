class Solution:
    def isPalindrome(self, n):
        orig = n
        rev = 0
        while n!=0:
            rev = rev*10 + n%10
            n = n//10
        return orig == rev
