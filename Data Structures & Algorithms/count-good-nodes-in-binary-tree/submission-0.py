# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.goodNumber = 0
        def dfs(root, currMax):
            if not root:
                return
            if root.val >= currMax:
                self.goodNumber += 1
            currMax = max(currMax, root.val)
            dfs(root.left, currMax)
            dfs(root.right, currMax)
        dfs(root, root.val)
        return self.goodNumber
        