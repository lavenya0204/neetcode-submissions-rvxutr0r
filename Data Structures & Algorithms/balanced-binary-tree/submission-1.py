# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h=0
        def maxDepth(root):
            if not root:
                return 0
            return 1 + max(maxDepth(root.left),maxDepth(root.right))
        if not root:
            return True
        diff=abs(maxDepth(root.left)-maxDepth(root.right))
        if diff>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)