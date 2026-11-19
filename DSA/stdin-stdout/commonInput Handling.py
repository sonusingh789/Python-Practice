import sys

input = sys.stdin.readline


def array(arr):
    lg = arr[0]
    for i in range(len(arr)):
        if arr[i] > lg:
            lg = arr[i]
    return lg


if __name__ == "__main__":
    # arr = list(map(int,input().split()))
    # print(array(arr))

    # number = int(input()) Single integer input
    # string = input() # single string input
    # arr = list(map(int,input().split())) multiple interger input in one line
    # string = list(map(str,input().split())) multiple string in single line
    # a,b = map(int,input().split())

    # array with size n
    # n=int(input())
    # arr = list(map(int,input().split()))

    # matrix input:

    # n,m = map(int,input().split())
    # matrix = []

    # for i in range(n):
    #     row = list(map(int,input().split()))
    #     matrix.append(row)

    # char array
    s = input()
    arr = list(s)
