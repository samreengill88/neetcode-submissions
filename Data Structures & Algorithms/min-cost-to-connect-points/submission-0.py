class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # PRIM's algorithim
        #### make adjacency list for undirected graph ####
        # node -> [cost, nei]
        adj = defaultdict(list) 
        n = len(points)
        # compare i to all other points 
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        total_cost = 0
        min_heap = [(0, 0)] # cost, point
        visit = set()

        while len(visit) < n: 
            cost, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            total_cost += cost 
            visit.add(node)

            for nei_cost, nei_node in adj[node]:
                if nei_node not in visit:
                    heapq.heappush(min_heap, (nei_cost, nei_node))

        return total_cost
    
    # TC:
    #   Building adj: O(n²)
    #   Heap operations: O(n² log n)
    #   Total: O(n² log n).
    # SC: 
    #   O(n²)