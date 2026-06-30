class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        # use minHeap
        # minHeap - always has k largest elements 

        self.minHeap = nums
        self.k = k

        # minHeap
        heapq.heapify(self.minHeap)

        # to have k largest elements in heap, pop min elements from heap until len(heap) == k
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # now minHeap has k largest elements

    def add(self, val: int) -> int:

        heapq.heappush(self.minHeap, val)
        
        # now heap has more than k elements so pop smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) 
        return self.minHeap[0]
        # what if heap is empty at the beginning - do not want to pop in that case -> so pop only if len is > k
        
# TC: init: O(n) for heapify, O(log n) for pop -> WC: O(n log n)
# SC: O(k) - minHeap always size k
