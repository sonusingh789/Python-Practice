class Solution:
    def anagramStrings(self, s, t):
        # your code goes here

        # st1 = list(s)
        # st2 = list(t)
        # st1.sort()
        # st2.sort()

        # return "".join(st1) == "".join(st2)

        if len(t) != len(s):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            count = freq.get(ch, 0)
            if count == 0:
                return False
            count -= 1
        return True
