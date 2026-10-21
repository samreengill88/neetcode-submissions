class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            
            # if the array is already sorted ex: [1, 2, 3, 4]
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            # ex 5 ≥ 3 you are left sorted portion--> min would be in right sorted 
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            # you are in right portion -- search left for the min element
            else:
                r = mid - 1
        return res