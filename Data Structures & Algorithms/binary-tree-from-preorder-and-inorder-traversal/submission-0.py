# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        # know: both preorder and inorder are non empty
        # first val in preorder is always root of the tree

        root = TreeNode(preorder[0])
        
        # get index of root in inorder -
        #       everything to the left of root in inorder is to left of tree and to the right is in right Tree

        mid = inorder.index(preorder[0]) # index of root in inorder

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root