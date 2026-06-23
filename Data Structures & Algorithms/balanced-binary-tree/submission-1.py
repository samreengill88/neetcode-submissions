# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root):
            if not root: # root is None so tree is balanced
                return [True, 0]

            isBalanced = False 

            # note left[0]: true or false whether it is balanced or not 
            # note left[1]: is height of left node
            left = dfs(root.left)
            right = dfs(root.right)
            height = 1 + (max(left[1], right[1]))

            # to check if tree is balanced 
            # check: 1) abs(left - right) is atmost 1 
            #        2) both left and right subtree are balanced
            if abs(left[1] - right[1]) <= 1 and left[0] and right[0]:
                isBalanced = True
            return [isBalanced, height]
        
        return dfs(root)[0]