# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # empty tree - return []
        if not root:
            return []

        # know: tree is not empty 

        q = deque()
        q.append(root)
        res = []
        # while q is not empty 
        while q:
            level_size = len(q)
            q_lst = []
            for i in range(level_size):
                n = q.popleft()
                q_lst.append(n.val)
            
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            res.append(q_lst)

        return res
