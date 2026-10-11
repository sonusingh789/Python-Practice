class Solution:
    def twoSum(self, nums, target):
        ind = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ind.append(i)
                    ind.append(j)
                    return ind

        return ind
