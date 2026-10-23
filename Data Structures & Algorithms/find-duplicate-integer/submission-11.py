class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # solving in space O(1)   
        # all values in nums are between 1 and n

        for i, num in enumerate(nums):

            # get index using num
            idx = abs(num) - 1

            if nums[idx] < 0:
                return abs(num)
            
            # negate the num at indx
            nums[idx] = -nums[idx]
        
        return -1

    # TC: O(n)
    # SC: O(1)