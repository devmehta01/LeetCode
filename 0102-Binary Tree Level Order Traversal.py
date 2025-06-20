# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([(root, 0)])
        answer = []

        while q:
            node, lev = q.popleft()

            if len(answer) == lev:
                answer.append([])
            
            answer[lev].append(node.val)

            if node.left:
                q.append((node.left, lev+1))
            if node.right:
                q.append((node.right, lev+1))
        
        return answer