


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        l = []
        while cur:
            l.append(cur)
            cur = cur.next
        l1 = []
        l2 = []
        for i in l:
            if i.val < x:
                l1.append(i)
            else:
                l2.append(i)
        l = l1 + l2
        for i in range(len(l) - 1):
            l[i].next = l[i + 1]
        l[-1].next = None
        return l[0]


