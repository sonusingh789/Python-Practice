class Solution:
    def secondMostFrequentElement(self, nums):

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())
        sec_high_freq = 0

        for value in freq.values():
            if value < max_freq and value > sec_high_freq:
                sec_high_freq = value

        ans = float("inf")  # => ∞

        # min(∞,x)=x
        for num in freq:
            if freq[num] == sec_high_freq:
                ans = min(ans, num)

        return ans if ans != float("inf") else -1
