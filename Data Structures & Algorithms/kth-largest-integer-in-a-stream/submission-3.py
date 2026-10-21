class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums 
        heapq.heapify(self.nums)

        # if k = 3, keep only 3 largest elements in heap
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:

        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]
# TC:
# let m be no of calls made to add 
# nums has atmost k items 
# push and pop on heap of size k - O(log k)
# with m calls to add --> O(m log k)

# SC:
# nums hold k items at a time -> O(k)

