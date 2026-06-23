# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # perform in-order traversal (left - root - right)
        arr = []
        def in_order_traversal(node):
            if not node:
                return 
            else:
                in_order_traversal(node.left)
                arr.append(node.val)
                in_order_traversal(node.right)
        
        # arr is in order travel so its sorted in ascending order
        in_order_traversal(root)
        return arr[k - 1] 


        # empty array
        # rec method: if root None return otherwise append root.val to arr
        # also do dfs(root.left) and dfs(root.right)
        # get arr[k - 1] to get the smallest
        # arr = []

        # def dfs(root):
        #     if not root:
        #         return 
            
        #     else:
        #         arr.append(root.val)
        #         dfs(root.left)
        #         dfs(root.right)
        
        # dfs(root)
        # arr.sort()
        # return arr[k - 1]