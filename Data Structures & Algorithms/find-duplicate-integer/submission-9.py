class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if nums[index] < 0:
                return abs(nums[i])
            
            nums[index] = nums[index] * -1
        
        return -1

        
        # for num in nums:
        #     idx = abs(num) - 1

        #     if nums[idx] < 0 :
        #         return abs(num)
                
        #     nums[idx] = -1 * nums[idx]
        #     # val is already -ve      

        # return -1