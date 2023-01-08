
a = 2*3
print(a)


b = 3**2
print(b)


nums = [int(n) for n in input().split()]
target = int(input())

if target in nums:
    print(nums.index(target))
else:
    nums += [target]
    nums.sort()
    print(nums.index(target))
