


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxi = -sys.maxsize - 1
        c = 0
        stack = [(root, maxi)]
        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                c += 1
                max_val = max(max_val, node.val)

            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))
        return c



