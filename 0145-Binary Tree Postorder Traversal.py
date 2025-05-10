# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        if not root:
            return ans
        left = self.postorderTraversal(root.left)
        if left:
            ans += left
        right = self.postorderTraversal(root.right)
        if right:
            ans += right
        ans += [root.val]

        return ans