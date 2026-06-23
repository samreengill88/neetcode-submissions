class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # using dfs
        # adjacency lst
        # start dfs from univisited node
        # every time dfs is started from new unvisited node - found one new component
        # track how many times 
        adjLst = {}
        for i in range(n):
            adjLst[i] = []
        for [u, v] in edges:
            adjLst[u].append(v)
            adjLst[v].append(u)
        
        component = 0
        visited = [False] * n

        def dfs(node):
            # stop if visited[node] is False
            visited[node] = True

            for nei in adjLst[node]:
                if not visited[nei]:
                    dfs(nei)


        for node in range(n):
            # for each unvisited node -> do dfs -> add component
            if visited[node] == False:
                dfs(node)
                component += 1
        
        return component