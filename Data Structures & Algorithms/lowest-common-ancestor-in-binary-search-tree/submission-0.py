# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # note it is a BST -> values on left < values on right
        if not root:
            return None
        
        curr = root 
        while curr:
            # if p, q is less than curr -> LCA is in left 
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr

    # TC: O(log n) for balanced and O(n) for skewed
    # SC: O(1)