


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        temp1 = ListNode()
        temp2 = ListNode()
        dummy1 = temp1
        dummy2 = temp2
        cur = head
        while cur:
            if cur.val < x:
                dummy1.next = cur
                dummy1 = dummy1.next
            else:
                dummy2.next = cur
                dummy2 = dummy2.next
            cur = cur.next
        dummy2.next = None
        dummy1.next = temp2.next
        return temp1.next

