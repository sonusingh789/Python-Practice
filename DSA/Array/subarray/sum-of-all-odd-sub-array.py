class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # # ans = []
        # # for i in range(len(arr)):
        # #     for j in range(i,len(arr)):
        # #         sumz = 0
        # #         count = 0
        # #         for k in range(i,j+1):
        # #             sumz += arr[k]
        # #             count +=1
        # #         if count%2 != 0:
        # #             ans.append(sumz)
        # # sum = 0
        # # for x in ans:
        # #     sum+=x
        # return sum

        total = 0

        for i in range(len(arr)):
            sumz = 0

            for j in range(i, len(arr)):
                sumz += arr[j]

                if (j - i + 1) % 2 != 0:
                    total += sumz

        return total
