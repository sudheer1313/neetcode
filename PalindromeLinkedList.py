


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = list()
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        return l[::-1] == l

