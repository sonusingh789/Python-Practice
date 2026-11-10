st = "abcdef"

for i in range(len(st)):
    for j in range(i, len(st)):
        for k in range(i, j + 1):
            print(st[k], end="")
        print()
