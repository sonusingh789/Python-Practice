class Solution:
    def isSorted(self, nums, count=0):

        if count >= len(nums) - 1:
            return True

        if nums[count] > nums[count + 1]:
            return False

        return self.isSorted(nums, count + 1)
