# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        self.traverse(root, ans)
        return ans
    
    def traverse(self, node, ans):
        if node.left:
            self.traverse(node.left, ans)
        ans.append(node.val)
        if node.right:
            self.traverse(node.right, ans)