

# リストの整数値を入力
head = list(map(int, input().split()))
# 重複を削除して出力
print(list(set(head)))
