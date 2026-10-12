class Solution:
    def rearrangeArray(self, nums):

        pos = []
        neg = []
        arr = []

        for x in nums:
            if x > 0:
                pos.append(x)
            else:
                neg.append(x)

        for i in range(len(pos)):
            arr.append(pos[i])
            arr.append(neg[i])

        return arr
