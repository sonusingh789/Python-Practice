num = 16
left = 1
right = num
ans = 0

while left <= right:
    mid = (left + right) // 2

    if mid * mid <= num:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
