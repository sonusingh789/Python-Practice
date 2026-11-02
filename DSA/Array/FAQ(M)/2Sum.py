class Solution:
    def twoSum(self, nums, target):
        # brute
        # ind = []

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             ind.append(i)
        #             ind.append(j)
        #             return ind

        # return ind

        hash_map = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in hash_map:
                return [hash_map[remaining], i]
            hash_map[num] = i
        return []

        # arr = [(num, i) for i, num in enumerate(nums)]
        # arr.sort()

        # i = 0
        # j = len(arr) - 1

        # while i < j:
        #     s = arr[i][0] + arr[j][0]

        #     if s == target:
        #         return [arr[i][1], arr[j][1]]
        #     elif s > target:
        #         j -= 1
        #     else:
        #         i += 1
