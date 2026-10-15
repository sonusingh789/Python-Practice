class Solution:
    def countOdd(self, arr, n):
        count = 0
        for x in arr:
            if x % 2 != 0:
                count += 1
        return count
