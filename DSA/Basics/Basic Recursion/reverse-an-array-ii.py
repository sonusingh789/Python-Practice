class Solution:
    def reverseArray(self, nums, count=0):
        if count >= len(nums) // 2:
            return nums

        temp = nums[count]
        nums[count] = nums[len(nums) - count - 1]
        nums[len(nums) - count - 1] = temp

        return self.reverseArray(nums, count + 1)
