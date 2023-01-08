strs = [n for n in input().split()]

strs.sort(key=len)
ans = ""
for i in range(len(strs[0])):
    count = 0
    for val in strs:
        if strs[0][:i+1] in val[:i+1]:
            count += 1
            if count == len(strs):
                ans = strs[0][:i+1]

print(ans)
