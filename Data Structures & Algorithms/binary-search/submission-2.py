class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            
            # target == nums[mid]
            else:
                return mid
        
        return -1 

    # TC: O(log n)
    # SC: O(1)
        