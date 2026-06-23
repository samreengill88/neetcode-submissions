"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # empty node - return None 
        if not node:
            return None
        
        # recurssively clone each node
        # if clone already exists - no need to make new clone, return its clone -> to track this hashmap oldToNew = {}
        
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            # clone dne - make clone of all the neighbors of node
            clone = Node(node.val)
            oldToNew[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            
            return clone
        
        return dfs(node)



        