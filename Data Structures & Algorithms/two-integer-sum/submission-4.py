class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        numsMap = {}
        for i, n in enumerate(nums):
            numsMap[n] = i
        
        for i, n in enumerate(nums):
            val = target - n
            if val in numsMap and numsMap[val] != i:
                return [i, numsMap[val]]
