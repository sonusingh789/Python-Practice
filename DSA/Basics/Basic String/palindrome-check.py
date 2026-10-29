class Solution:
    def palindromeCheck(self, s):
        # your code goes here

        st = list(s)

        i = 0
        j = len(s) - 1

        while i < j:
            temp = st[i]
            st[i] = st[j]
            st[j] = temp

            i += 1
            j -= 1

        return "".join(st) == s
