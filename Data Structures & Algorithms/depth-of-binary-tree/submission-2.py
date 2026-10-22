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

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



# TC: each node visited once -> O(n)
# SC:  - in wc tree is compeletely skewed - tree is a straight line -> so n calls on the           rec stack -> so O(n)
#       -  if tree balanced -> O(log n)