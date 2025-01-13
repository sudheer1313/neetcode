

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        nodes=[]

        while cur:
            nodes.append(cur)
            cur=cur.next

        l=len(nodes)

        for i in range(0, l, k):
            if l - i < k:
                break
            nodes[i:i + k]=reversed(nodes[i:i + k])

        for i in range(l - 1):
            nodes[i].next=nodes[i + 1]
        nodes[-1].next=None

        if nodes:
            return nodes[0]
        else:
             return None
