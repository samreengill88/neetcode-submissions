class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # 1. build adj_lst for undirected graph 
        # 2. if node is not in visit -> run dfs(node) and inc no. of components


        adj_lst = defaultdict(list)
        for u, v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)
        
        visit = set()

        def dfs(node):
            
            visit.add(node)
            for nei in adj_lst[node]:
                if nei not in visit:
                    dfs(nei)

        count = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                count += 1
        return count 
