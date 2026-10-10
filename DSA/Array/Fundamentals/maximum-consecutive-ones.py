class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_con = 0
        tempCount = 0

        for x in nums:
            if x == 1:
                tempCount += 1
            else:
                if tempCount > max_con:
                    max_con = tempCount
                tempCount = 0

        if tempCount > max_con:
            max_con = tempCount

        return max_con
