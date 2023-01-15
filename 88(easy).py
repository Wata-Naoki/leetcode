

num1 = [int(x) for x in input().split()]
m = int(input())

num2 = [int(x) for x in input().split()]
n = int(input())

num1 += num2
# print(num1)

num1 = [x for x in num1 if x != 0]
num1.sort()

print(num1)
