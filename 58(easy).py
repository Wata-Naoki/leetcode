n = input().strip()
# リートコードでは再代入する必要あり
# def lengthOfLastWord(self, s: str) -> int:
# s = s.strip()のように
ind = n.rfind(' ')
print(len(n[ind+1:]))
