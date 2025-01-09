


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_list = []
        for i in lists:
            while i:
                new_list.append(i.val)
                i = i.next
        new_list = sorted(new_list)
        dummy = ListNode()
        temp = dummy
        for i in new_list:
            temp.next = ListNode(i)
            temp = temp.next
        return dummy.next


