# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      
        # BFS
        if not root:
            return []
        
        q = deque()
        q.append(root)

        res = []

        while q:
            level_size = len(q)
            level = []

            for i in range(level_size):
                node = q.popleft()
                level.append(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:

                    q.append(node.right)
            res.append(level)
        
        return res

# TC: each node is enqueued and dequeued exactly once with constant work.
# SC: q size-> O(n)