class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        st = set()
        for x in nums:
            st.add(x)

        sort_d = sorted(st)
        for i, value in enumerate(sort_d):
            nums[i] = value

        return len(sort_d)
