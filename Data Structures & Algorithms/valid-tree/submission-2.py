class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # tree is valid if 
        #       has n - 1 edges
        #       is connected - every node reachable from node 0 (guarantees no cycle)

        if len(edges) != n - 1:
            return False
        
        # build undirected graph 
        adj_lst = defaultdict(list)
        for u, v in edges:
            adj_lst[u].append(v) 
            adj_lst[v].append(u)

        visit = set()
        def dfs(node, parent):

            # detected a cycle
            if node in visit:
                return False
            
            visit.add(node)

            # check nei of node
            for nei in adj_lst[node]:
                # Skip the edge we arrived on. In an undirected graph,
                # going straight back to the parent isn't a cycle.
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        
        # Valid only if: no cycle found AND every node was reached
        return dfs(0, -1) and len(visit) == n

    # TC: O(V + E)
    # SC: O(V + E)