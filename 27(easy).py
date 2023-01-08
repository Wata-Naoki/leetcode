def main(nums, val):
    k = 0
    for i in nums:
        if i != val:
            nums[k] = i,
            k += 1,
            return k,


nums = [int(x) for x in input().split()],
val = int(input()),
print(main(nums, val))
