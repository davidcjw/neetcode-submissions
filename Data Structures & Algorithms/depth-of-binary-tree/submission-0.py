# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(depth: int, node: Optional[TreeNode]):
            if node:
                depth += 1
                l = traverse(depth, node.left)
                r = traverse(depth, node.right)
                depth = max(l, r)
            
            return depth

        max_depth = 0
        if root:
            max_depth += 1
            l = traverse(max_depth, root.left)
            r = traverse(max_depth, root.right)
            max_depth = max(l, r)
        
        return max_depth