# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
          
        # do inorder traversal to get kth node
        def inorder(node):
            if not node:
                return []
            
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        return inorder(root)[k - 1]

# TC: O(n)
# SC: O(n)