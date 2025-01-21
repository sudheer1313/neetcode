


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l_a = [root]

        def lca(root):
            l_a[0] = root
            if not root:
                return
            if root.val > p.val and root.val > q.val:
                lca(root.left)
            elif root.val < p.val and root.val < q.val:
                lca(root.right)
            else:
                return

        lca(root)
        return l_a[0]


