class Solution:
    def rotateArrayByOne(self, nums):

        temp = nums[0]
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]
        nums[len(nums) - 1] = temp


# alt

# class Solution:
#     def rotateArrayByOne(self, nums):

#         k = 1%len(nums)
#         arr = []
#         arr = nums[k:] + nums[:k]

#         for i , value in enumerate(arr):
#             nums[i] = value
