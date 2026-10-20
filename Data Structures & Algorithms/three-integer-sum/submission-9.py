class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
     
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        target = 0

        res = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # now i is fixed find l and r such that i + l + r =0 
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr_sum = nums[l] + nums[r] + n
                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    # valid triplet found so i + l + r = 0 
                    # now i is fixed, move either l or r 
                    # i fixed, r fixed, move l by 1 
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    # check for duplicate triplet
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1                    
        return res

# TC: 
#   - O(n log n) for sort 
#   - all values in nums are distinct 
#   - while loop traverse atmost n elements for each outer loop iteration 
#   - so total O(n log n) + O(n^2) == O(n^2)
# SC: O(1)
        