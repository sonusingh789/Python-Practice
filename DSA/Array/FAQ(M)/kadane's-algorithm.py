class Solution:
    def maxSubArray(self, nums):

        # brute force
        # max_value = float("-inf")
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         if sum > max_value:
        #             max_value = sum
        # return max_value

        sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            sum = max(nums[i], sum + nums[i])
            max_sum = max(max_sum, sum)

        return max_sum
