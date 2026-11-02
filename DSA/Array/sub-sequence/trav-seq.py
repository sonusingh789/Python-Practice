def genSubSequence(arr):
    ans = [[]]
    for num in arr:
        new = []
        for sub in ans:
            new.append(sub + [num])
        ans = ans + new
    return ans


print(genSubSequence([1, 2, 3]))
