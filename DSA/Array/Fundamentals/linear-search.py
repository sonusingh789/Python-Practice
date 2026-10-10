class Solution:
    def linearSearch(self, nums, target):
        for i, value in enumerate(nums):
            if value == target:
                return i
        return -1
