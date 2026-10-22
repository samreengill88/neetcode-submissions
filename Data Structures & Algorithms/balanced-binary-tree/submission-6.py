# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # from each child we need [is_balanced ,height]
        # so need different dfs(node)
        def dfs(node):
            
            if not node:
                return [True, 0] # node is balanced at height is 0
            
            left = dfs(node.left)
            right  = dfs(node.right)

            # check if L and R are balanced
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # return is_balanced and height
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
    

# TC: each node visited once -> O(n)
# SC:  - in wc tree is compeletely skewed - tree is a straight line -> so n calls on the           rec stack -> so O(n)
#       -  if tree balanced -> O(log n)