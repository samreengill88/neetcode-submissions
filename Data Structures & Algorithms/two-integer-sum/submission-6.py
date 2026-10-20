class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # start with first num 
        # check if target - num is in nums but do not include num 
        
        indices = {} # val -> index
        for i, n in enumerate(nums):
            indices[n] = i

        for i in range(len(nums)):
            val = target - nums[i]
            if val in indices and i != indices[val]:
                return [i, indices[val]]
        return []


        # TC: O(n)
        # SC: O(n) all values in nums are distinct 
        # if duplicate in nums, indices overwrite index 
        # it works it if check in loop