
# digits = [int(n) for n in input().split()]

# new_digits = digits
# if new_digits[len(new_digits)-1] == 9:
#     new_digits[len(new_digits)-1] = 1
#     new_digits.append(0)
# else:
#     new_digits[len(new_digits)-1] = new_digits[len(new_digits)-1]+1

# print(new_digits)


# a = [1, 2, 3, 9, 6, 4]
# print(a[(len(a)-1)-2])


digits = [int(n) for n in input().split()]

length = len(digits) - 1
while digits[length] == 9:
    digits[length] = 0
    length -= 1
if (length < 0):
    digits = [1] + digits
else:
    digits[length] += 1
print(digits)
