import sys

input = sys.stdin.readline


def genrateSubString(st):
    allstr = []
    for i in range(len(st)):
        sti = ""
        for j in range(i, len(st)):
            sti += st[j]
            allstr.append(sti)
    return allstr


if __name__ == "__main__":
    st = input().strip()
    print(genrateSubString(st))
