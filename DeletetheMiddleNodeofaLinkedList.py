


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1
        m = l // 2
        prev = head
        cur1 = head
        for i in range(m):
            prev = cur1
            cur1 = cur1.next
        prev.next = cur1.next
        return head




