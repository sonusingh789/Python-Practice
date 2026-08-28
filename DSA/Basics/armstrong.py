
def is_arm_strong(n):
    nums = str(n)
    sum = 0
    for i in range(len(nums)):
        sum = sum + (int(nums[i])**len(nums))
    nums2 = str(sum)
    if(nums == nums2):
        return True
    return False

print(is_arm_strong(121))
print(is_arm_strong(151))


