class Solution:
    def frequencySort(self, s):
        freq = {}

        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
        morpt = []

        for value in freq.values():
            morpt.append(value)

        morpt.sort(reverse=True)

        used = set()
        ans = []

        for i in range(len(morpt)):
            for key, value in sorted(freq.items()):
                if value == morpt[i] and key not in used:
                    ans.append(key)
                    used.add(key)
        return ans
