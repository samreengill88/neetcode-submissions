class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        

        if len(edges) != n - 1:
            return False
        
        # build undirected graph 
        adj_lst = defaultdict(list)
        for u, v in edges:
            adj_lst[u].append(v) 
            adj_lst[v].append(u)
        
        visit = set()

        # check if no cycle - dfs
        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)
            
            # check neighbors
            for nei in adj_lst[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True


        return dfs(0, -1) and len(visit) == n