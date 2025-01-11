


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        c = 0
        while l1 or l2 or c:
            if l1 is not None:
                value1 = l1.val
                l1 = l1.next
            else:
                value1 = 0
            if l2 is not None:
                value2 = l2.val
                l2 = l2.next
            else:
                value2 = 0
            value3 = value1 + value2 + c
            d = value3 % 10
            c = value3 // 10
            temp.next = ListNode(d)
            temp = temp.next

        return dummy.next



