class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = 1
        suffix[n - 1] = 1
        
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        res = [0] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res  
    
    # TC: O(n)
    # SC: O(n)
    
            
