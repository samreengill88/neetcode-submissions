# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # both empty - return True 
        # empty subroot and not empty root - return True
        # empty root and not empty subroot - return False
        ### know: root and subroot - not empty 

        # both root and subroot empty
        if not root and not subRoot:
            return True
        
        # subroot empty, root not empty
        if not subRoot and root:
            return True
        
        # root empty, subroot not empty
        if not root and subRoot:
            return False

        # know both root and subRoot not empty
        # when root.val matches subRoot.val - check if its the sameTree
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        # p and q - empty
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
            
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


        