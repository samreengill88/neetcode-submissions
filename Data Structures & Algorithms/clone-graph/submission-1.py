"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}
        
        def dfs(node):
            # node is already cloned  -> reuse the existing copy
            if node in old_to_new:
                return old_to_new[node]
            
            # make the copy
            clone = Node(node.val)
            old_to_new[node] = clone
            
            # Copy each neighbour (or fetch its existing copy)
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone
        return dfs(node)

    # TC:
    #   Cloning nodes → O(V)
    #   Following edges → O(E)
    # total : O(V) + O(E)
    # SC:
    #   old_to_new one entry per node -> O(V)
    #   rec stack - wc long chain -> O(V)
    #   total: O(V)