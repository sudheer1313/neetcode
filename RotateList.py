


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        tail = head
        l = 1
        while tail.next:
            l += 1
            tail = tail.next
        k = k % l
        cur1 = head
        for i in range(l - k - 1):
            cur1 = cur1.next
        if k == 0:
            return head
        dummy = cur1.next
        cur1.next = None
        tail.next = head
        return dummy




