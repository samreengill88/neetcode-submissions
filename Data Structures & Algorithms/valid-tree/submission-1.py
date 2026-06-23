class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # tree has exactly (n-1) edges
        if len(edges) != n - 1:
            return False
        
        # detect cycle 
        # adjacency list
        adjList = {}
        for i in range(n):
            adjList[i] = []
        # we have undirected graph
        for [u, v] in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()

        def dfs(node, parent):
            # stop if node in visit
            if node in visit:
                return False
            
            # add node to visit
            visit.add(node)

            # check edges in adjList
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        dfs(0, -1)
        return len(visit) == n