# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        if abs(l-r) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
