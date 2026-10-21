class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            # nums = [4, 5, 6, 7, 0, 1, 2]
            mid = (l + r) // 2
        
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            # [4, 5, 6, 7] l = 4, mid = 7
            if nums[l] <= nums[mid]: # 4 ≤ 7
                if target > nums[mid] or target < nums[l]: # if target = 8 or target = 3
                    l = mid + 1
                else: # target = 6
                    r = mid - 1
            # right sorted portion
            # [0, 1, 2]
            else: # mid = 1, r = 2
                if target < nums[mid] or target > nums[r]: # target is 0 or target 3
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1

# TC: O(log n)
# SC: O(1)