ans_list = []
list1 = [int(n) for n in input().split()]
list2 = [int(n) for n in input().split()]

ans_list += list1+list2
ans_list.sort()
print(ans_list)
