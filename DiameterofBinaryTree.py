


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]

        def diameter(root):
            if root is None:
                return 0
            left = diameter(root.left)
            right = diameter(root.right)
            maxi[0] = max(maxi[0], left + right)
            return 1 + max(left, right)

        diameter(root)
        return maxi[0]

