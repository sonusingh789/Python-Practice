class Solution:
    def sumHighestAndLowestFrequency(self, nums):

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())

        min_freq = min(freq.values())

        return max_freq + min_freq
