class Solution:
    def majorityElement(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        max_freq = max(freq.values())

        for key, val in freq.items():
            if val == max_freq:
                return key
