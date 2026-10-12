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




# class Solution:
#     def findMaxConsecutiveOnes(self, nums):
#         count = 0
#         max_con = 0

#         for i in range(len(nums)):
#             if nums[i] == 1:
#                 count += 1
#                 max_con = max(max_con, count)
#             else:
#                 count = 0

#         return max_con
