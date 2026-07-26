# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        if a node has right child, node.right is the right view
        - track each level's rightmost node

        do regular recursive DFS and traverse right child first if any;
        then store itself in the previous level
        """
        levels = defaultdict(list)  # {0: [1], 1: [2,3]}

        def dfs(node, level):
            if not node:
                return
            
            if node.left:
                dfs(node.left, level+1)
            levels[level].append(node.val)
            if node.right:
                dfs(node.right, level+1)

        dfs(root, 0)
        if not levels:
            return []

        res = []
        maxLevel = max(levels.keys())
        for i in range(maxLevel+1):
            res.append(levels[i][-1])
        return res
