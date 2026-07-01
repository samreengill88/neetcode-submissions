from heapq import heapify, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        # calculate dist of points from origin
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)

        res = []
        while len(res) != k:
            dist, x, y= heapq.heappop(minHeap)
            res.append([x, y])
        
        return res