class Solution:
    def reverse(self, arr: list, n: int) -> None:
        # return arr.reverse()

        # for i in range(n // 2):
        #     temp = arr[i]
        #     arr[i] = arr[n - 1 - i]
        #     arr[n - 1 - i] = temp

        i = 0
        j = n - 1

        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            i += 1
            j -= 1
