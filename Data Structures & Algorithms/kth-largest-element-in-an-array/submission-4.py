class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

# TC: heapify - O(n)
#  while loop until we have k items in nums so runs n - k times each heappop takes O(log n) == O(n-k logn )
# in worst case k = 1 find maximum . Then you pop n − 1 times, which gives
# Total -->  O(n + n log n) = O(n log n).
# SC: 
#   O(1)