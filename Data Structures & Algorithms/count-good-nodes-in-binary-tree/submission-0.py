# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxValInPath):
            if not node:
                return 0
            
            numGoodNodesInPath = 1 if node.val >= maxValInPath else 0
            maxValInPath = max(maxValInPath, node.val)
            left = dfs(node.left, maxValInPath)
            right = dfs(node.right, maxValInPath)
            return numGoodNodesInPath + left + right

        return dfs(root, root.val)