class Solution:
    def arraySum(self, nums, count=0):

        if count >= len(nums):
            return 0
        return nums[count] + self.arraySum(nums, count + 1)
