class Solution:
    def rotateArray(self, nums, k: int) -> None:
        k = k % len(nums)
        # arr = []
        # arr = nums[k:] + nums[:k]
        # for i, value in enumerate(arr):
        #     nums[i] = value

        for i in range(k):
            temp = nums[0]

            for i in range(len(nums) - 1):
                nums[i] = nums[i + 1]

            nums[len(nums) - 1] = temp
