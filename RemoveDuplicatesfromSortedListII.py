


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head
        dummy = ListNode()
        temp = dummy
        while cur:
            arr.append(cur.val)
            cur = cur.next
        d = Counter(arr)
        for key, val in d.items():
            if val == 1:
                temp.next = ListNode(key)
                temp = temp.next
        return dummy.next



