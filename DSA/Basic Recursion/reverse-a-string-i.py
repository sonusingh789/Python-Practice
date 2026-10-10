class Solution:
    def reverseString(self, s, count=0):
        if count >= len(s) // 2:
            return s

        temp = s[count]
        s[count] = s[len(s) - 1 - count]
        s[len(s) - 1 - count] = temp

        return self.reverseString(s, count + 1)
