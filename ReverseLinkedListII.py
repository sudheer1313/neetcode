


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        li = list()
        cur = head
        while cur:
            li.append(cur)
            cur = cur.next
        l = left - 1
        r = right - 1
        while l < r:
            li[l], li[r] = li[r], li[l]
            l += 1
            r -= 1
        for i in range(len(li) - 1):
            li[i].next = li[i + 1]
        li[-1].next = None
        return li[0]


