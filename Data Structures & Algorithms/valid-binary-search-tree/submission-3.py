# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(node, left, right):

            if not node:
                return True
            
            if not left < node.val < right:
                return False
            
            # for left: right bound(max) is capped 
            left_valid = is_valid(node.left, left, node.val)

            # for right: left bound(min) is capped
            right_valid = is_valid(node.right, node.val, right)

            return left_valid and right_valid

        return is_valid(root, float("-inf"), float("inf"))

    
    # TC: O(n)
    # SC: O(n)