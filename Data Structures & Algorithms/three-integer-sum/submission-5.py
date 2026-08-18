class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
     
        nums.sort()
        res = []

        for i,num in enumerate(nums):

            # to avoid duplicates
            if i > 0 and num == nums[i - 1]:
                continue

            # set l and r pointers 
            l = i + 1
            r = len(nums) - 1

            while l < r:
                currSum = num + nums[l] + nums[r]
                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res