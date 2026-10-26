class Solution:
    def GCD(self, n1, n2):
        fact1 = []
        for i in range(1, n1 + 1):
            if n1 % i == 0:
                fact1.append(i)

        fact2 = []
        for i in range(1, n2 + 1):
            if n2 % i == 0:
                fact2.append(i)
        common = []

        i = 0
        j = 0

        while i < len(fact1) and j < len(fact2):
            if fact1[i] == fact2[j]:
                common.append(fact1[i])
                i += 1
                j += 1
            elif fact1[i] > fact2[j]:
                j += 1
            else:
                i += 1
        gcd = max(common)
        return gcd
