class Solution:
    def leaders(self, nums):
        leader = []

        for i in range(len(nums)):
            check = True

            for j in range(i + 1, len(nums)):
                if nums[i] <= nums[j]:
                    check = False
                    break

            if check == True:
                leader.append(nums[i])

        return leader
