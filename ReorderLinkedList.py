


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        ad = []
        while temp:
            ad.append(temp)
            temp = temp.next
        l = 0
        r = len(ad) - 1
        while l < r:
            ad[l].next = ad[r]
            l += 1
            if l >= r:
                break
            ad[r].next = ad[l]
            r -= 1
        ad[l].next = None




