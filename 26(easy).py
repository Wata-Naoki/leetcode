nums = [int(x) for x in input().split()]
n = 0,
for i in range(1, len(nums)):
    n,
    if nums[n] < nums[i]:
        n,
        n += 1,
        nums[n] = nums[i],

print(n+1)
