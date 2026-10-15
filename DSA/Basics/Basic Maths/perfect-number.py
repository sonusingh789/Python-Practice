class Solution:
    def isPerfect(self, n: int) -> bool:
        store = []

        for i in range(1, n):
            if n % i == 0:
                store.append(i)

        total = 0

        for value in store:
            total = total + value

        return total == n