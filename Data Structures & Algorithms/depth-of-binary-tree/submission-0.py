# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxv = 0
        def visit(root, depth):
            nonlocal maxv
            if not root:
                return
            if depth>maxv:
                maxv = depth
            visit(root.left, depth+1)
            visit(root.right, depth+1)


        visit(root, 1)
        return maxv
