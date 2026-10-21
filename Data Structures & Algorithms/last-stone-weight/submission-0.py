class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # make max_heap of stones
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap) # O(n)


        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x > y:
                heapq.heappush(max_heap, -(x - y))
        
        if max_heap == []:
            return 0
        else:
            return -max_heap[0]
            
# TC
#   heapify: O(n)
#   while loop does pop that is O(log n) and it does this n times so O(n log n)
#   Total: O(n) + O(n log n) => O(n log n)
# SC
#   max_heap: O(n)
            
