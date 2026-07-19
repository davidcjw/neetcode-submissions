# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder -> first node is left most node of left subtree
        # preorder -> first node is the root node
        # we can find the left and right subtree split in inorder
        # using root node derived from preorder
        if not preorder or not inorder:
            return None

        rootVal = preorder[0]
        root = TreeNode(rootVal)
        rootIdxInInorder = inorder.index(rootVal)
        root.left = self.buildTree(preorder[1:rootIdxInInorder+1], inorder[:rootIdxInInorder])
        root.right = self.buildTree(preorder[rootIdxInInorder+1:], inorder[rootIdxInInorder+1:])
        return root
