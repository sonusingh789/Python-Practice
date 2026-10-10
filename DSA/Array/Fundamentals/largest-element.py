class Solution:
    def largestElement(self, nums):
        lg = nums[0]

        for x in nums:
            if x > lg:
                lg = x
        return lg
