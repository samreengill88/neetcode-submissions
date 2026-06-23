class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums = [-1,0,1,2,-1,-4]
        # sort(nums) : [-4, 0, -1, -1, 0, 1, 2]
        # if the first index is +ve, then cam'e get 0 
        # get the element on index 1 (target)
        # use two pointer l and r to get to target

        nums.sort()
        res = []

        for i, n in enumerate(nums):
            # first element is +ve
            if n > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]: # first index is same as 0th index, continue until you get a distict no
                continue

                # use two pointer from two sum

            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    # found triplets sum to 0
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while(nums[l] == nums[l - 1] and l < r):
                        l += 1
        return res
                    

                     




        

