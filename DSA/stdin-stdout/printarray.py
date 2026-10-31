import sys

input = sys.stdin.readline


def printr(arr):
    for i in range(len(arr)):
        if i == 0:
            print("[", end="")

        if i == len(arr) - 1:
            print(arr[i], end="")
            print("]")
        else:
            print(arr[i], end=", ")


if __name__ == "__main__":
    ar = list(map(int, input().strip()))
    printr(ar)
