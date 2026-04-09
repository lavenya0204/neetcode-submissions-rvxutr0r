# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res=0
    def maxDepth(self,root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        self.res=max(self.res,self.maxDepth(root.right)+self.maxDepth(root.left))
        if root.left:
            self.diameterOfBinaryTree(root.left)
        if root.right:
            self.diameterOfBinaryTree(root.right)
        return self.res
        