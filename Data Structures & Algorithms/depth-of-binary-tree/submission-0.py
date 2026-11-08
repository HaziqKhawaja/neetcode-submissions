# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth_left, depth_right = 1, 1
        if root is None:
            return 0
        if root.left is not None:
            depth_left = self.maxDepth(root.left) + 1
        if root.right is not None:
            depth_right = self.maxDepth(root.right) + 1
        return max(depth_left, depth_right)