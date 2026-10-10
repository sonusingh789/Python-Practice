class Solution:
    def mostFrequentElement(self, nums):

        freq = {}

        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())

        ans = float("inf")
        for num in freq:
            if freq[num] == max_freq:
                ans = min(ans, num)
        return ans
