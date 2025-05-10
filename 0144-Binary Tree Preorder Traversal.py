# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        if not root:
            return ans
        ans+=[root.val]
        left = self.preorderTraversal(root.left)
        if left:
            ans += left
        right = self.preorderTraversal(root.right)
        if right:
            ans += right
        return ans