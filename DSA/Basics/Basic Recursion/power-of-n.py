def myPow(num, n, count=0, result=1):

    if count == n:
        return result
    return myPow(num, n, count + 1, result * num)

print(myPow(2, 3))


# handles small numners only
# class Solution(object):
#     def myPow(self, x, n, count=0, result=1):
#         if count == abs(n):
#             return result

#         if n > 0:
#             return self.myPow(x, n, count + 1, result * x)
#         else:
#             return self.myPow(x, n, count + 1, result / x)
