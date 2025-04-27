# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        def check(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and check(l.left,r.right) and check(l.right,r.left)
        return check(root.left, root.right)