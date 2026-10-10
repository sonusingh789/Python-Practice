class Solution:
    def secondLargestElement(self, nums):
        lg = nums[0]
        sec_lg = -1

        for x in nums:
            if x > lg:
                lg = x

        for x in nums:
            if x < lg and x > sec_lg:
                sec_lg = x

        return sec_lg
