# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(root):
            if not root:
                return 0 
            
            left = height(root.left)
            right = height(root.right)

            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
            
        height(root)
        return self.diameter

# TC: each node visited once -> O(n)
# SC:  - in wc tree is compeletely skewed - tree is a straight line -> so n calls on the           rec stack -> so O(n)
#       -  if tree balanced -> O(log n)