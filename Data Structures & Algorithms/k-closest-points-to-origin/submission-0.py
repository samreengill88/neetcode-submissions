from heapq import heapify, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            minHeap.append([dist, x, y])

        # make a heap, when you call heapify by deafult get min heap based on first element in sublist

        heapify(minHeap) # min heap is sorted based on distance
        res =[]
        while k > 0:
            dist, x, y = heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res