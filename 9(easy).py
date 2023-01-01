class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = False
        str_x = str(x)
        if str_x == "".join(reversed(str_x)):
            flag = True
        else:
            flag = False
        return flag


x = int(input())
print(Solution().isPalindrome(x))
