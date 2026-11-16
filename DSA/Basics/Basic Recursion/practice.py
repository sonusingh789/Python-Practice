def oneton(n):
    if n == 0:
        return
    oneton(n - 1)
    print(n)


# oneton(10)


def oneton(n):
    if n == 0:
        return
    print(n)
    oneton(n - 1)


# oneton(10)


def sumofn(n):
    if n == 0:
        return 0
    return n + sumofn(n - 1)


# print(sumofn(10))


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


# print(fact(5))


arr = [1, 2, 3, 4, 5, 6, 7]


def reverse(arr, i=0, j=len(arr) - 1):
    if i >= j:
        return
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    reverse(arr, i + 1, j - 1)


# reverse(arr)
# print(arr)

arr = [1, 2, 3, 4, 5, 6, 7]


def reverse(arr, i=0):
    if i >= len(arr) // 2:
        return
    temp = arr[i]
    arr[i] = arr[len(arr) - i - 1]
    arr[len(arr) - i - 1] = temp
    reverse(arr, i + 1)


# reverse(arr)
# print(arr)


num = [1, 0, 0, 1]


def palindrom(num, i=0, ispalindrom=True):
    if i >= len(num) // 2:
        return ispalindrom
    if num[i] != num[len(num) - i - 1]:
        return False
    return palindrom(num, i + 1, ispalindrom)


print(palindrom(num))


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)
print(fibo(5))
