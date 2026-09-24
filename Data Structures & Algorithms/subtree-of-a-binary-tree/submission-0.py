# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkIfSubRoot(r1, r2, final) -> bool:
            if final:
                return True
            if not r1:
                return final
            if r1.val == r2.val:
                final = compareTree(r1, r2)
            return final or checkIfSubRoot(r1.left, r2, final) or checkIfSubRoot(r1.right, r2, final)
            
        def compareTree(r1, r2) -> bool:
            if not r1 and not r2:
                return True
            if r1 and r2:
                if r1.val != r2.val:
                    return False
                return compareTree(r1.left, r2.left) and compareTree(r1.right, r2.right)
            else:
                return False

        return checkIfSubRoot(root, subRoot, False)