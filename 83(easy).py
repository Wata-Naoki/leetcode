

# リストの整数値を入力
# head = list(map(int, input().split()))
# 重複を削除して出力
# print(list(set(head)))


def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return None
    if head.next == None:
        return head
        prev = head
        curr = head.next
    while curr != None:
        if curr.val == prev.val:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return head


head = list(map(int, input().split()))

print(deleteDuplicates(head=head))
