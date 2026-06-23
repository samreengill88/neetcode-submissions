class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort numbers to avoid duplicate pairs
        # set a and then find l and r using 2 pointer 

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # if second num is same as the previous one - same number duplicate move forward by 1
            if i > 0 and a == nums[i - 1]:
                continue
            
            # two pointers, target = 0
            l = i + 1
            r = len(nums) - 1
            while l < r:
                currSum = a + nums[l] + nums[r]
                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    # a + b + c = 0
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

        