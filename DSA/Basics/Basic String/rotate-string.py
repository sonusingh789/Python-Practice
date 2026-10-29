class Solution:
    def rotateString(self, s, goal):
        # your code goes here
        arr = []

        for ch in s:
            arr.append(ch)

        for i in range(len(arr)):
            st = arr.pop(0)
            arr.append(st)
            if "".join(arr) == goal:
                return True

        return False
