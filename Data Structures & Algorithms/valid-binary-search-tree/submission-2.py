# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # do dfs
        # need a value to compare each node to 
        #       each node should be within a certain range, has UB and LB
        #       - so need another function

        def isValid(node, left, right):
            # empty tree
            if not node:
                return True
            
            # bounds for node.val (left, right) 
            if not(left < node.val < right):
                return False
            
            return isValid(node.left, left, node.val ) and isValid(node.right, node.val, right)


        return isValid(root, float("-inf"), float("inf"))