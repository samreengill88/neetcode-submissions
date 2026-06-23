# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # need max_val to compare every value with 
        # starting with root - assume root.val is max_val
        def dfs(node, max_val) -> int:
            # empty tree
            if not node:
                return 0
            
            count = 0
            if node.val >= max_val:
                count = 1
            
            # update max val
            new_max_val = max(node.val, max_val)

            return count + dfs(node.left, new_max_val) + dfs(node.right, new_max_val)

        return dfs(root, root.val)