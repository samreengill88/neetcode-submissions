# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        # calculate height
        def height(root):
            nonlocal res
            if not root: 
                return 0
        
            left = height(root.left)
            right = height(root.right)
            res = max(res, left + right) # update res before returning, res is max of res and left + right
            return 1 + max(left, right) # this is the height of tree

        height(root)
        return res
