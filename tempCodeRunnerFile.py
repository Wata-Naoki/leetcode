nums = [int(n) for n in input().split()]
target = int(input())

if target in nums:
    print(nums.index(target))
else:
    nums += [target]
    nums.sort()
    print(nums.index(target))