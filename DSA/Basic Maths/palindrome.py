def palindrome_check(n):
    num1 = str(n)  ## strings are immmutable in python
    num2 = list(num1)
    i = 0
    j = len(num1) - 1
    while i < j:
        temp = num2[i]
        num2[i] = num1[j]
        num2[j] = temp
        i += 1
        j -= 1
    if num1 == ''.join(num2):
        return True
    return False
print(palindrome_check(121))