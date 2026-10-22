# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and subRoot:
            return False
        
        if not subRoot:
            return True
        
        # know: root and subRoot - not empty
        # does the tree starting at this node match?
        if self.isSameTree(root, subRoot):
            return True
        
        # otherwise, try starting points in the left or right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):

        # both empty
        if not p and not q:
            return True
        # p emty, q not empty or p not empty, q empty
        if (not p and q) or (p and not q):
            return False
        
        # know: both p and q are non-empty
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# m = nodes in root and n = nodes in subRoot.
# TC: O(m * n) - isSubtree → O(m) calls, sameTree → up to O(n) per call
# SC: O(m + n)