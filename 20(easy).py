class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in dict.values():
                stack.append(c)
            elif stack != [] and dict[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []


#   '(', ')', '{', '}', '[' and ']'のどれかor組み合わせ。ex) "()[]{}"
s = input()
ans = Solution().isValid(s)
print(ans)
