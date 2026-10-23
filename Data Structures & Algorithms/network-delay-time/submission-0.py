class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # build graph 
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((w, v))

        min_heap = [(0, k)] # [weight to get to node k, k]

        time = 0 
        visit = set()

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            time = max(time, w1)

            # neighbor of node n1
            for w2, n2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        
        if len(visit) == n:
            return time
        else: 
            return -1
