# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findHeight(root, height):
            if not root:
                return 0

            return 1 + max(findHeight(root.right, height + 1), findHeight(root.left, height + 1))
        
        return findHeight(root, 0)