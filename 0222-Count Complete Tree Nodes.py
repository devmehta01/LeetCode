# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def leftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def rightHeight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        if not root:
            return 0

        lh = leftHeight(root)
        rh = rightHeight(root)

        if lh == rh:
            # Tree is a perfect binary tree
            return 2**lh - 1
        else:
            # Not perfect, recurse on left and right
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)