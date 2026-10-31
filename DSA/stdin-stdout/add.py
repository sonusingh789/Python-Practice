import sys

input = sys.stdin.readline


def add(x, y):
    return x + y


if __name__ == "__main__":
    x = int(input())
    y = int(input())

    sum = add(x, y)
    print(sum)
