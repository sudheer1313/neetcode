


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        temp = head
        c = 0
        while temp:
            temp = temp.next
            c += 1
        cur = head
        prev = head
        if c == n:
            return head.next

        for i in range(c):
            if n == c:
                prev.next = cur.next
                break
            c -= 1
            prev = cur
            cur = cur.next
        return head



