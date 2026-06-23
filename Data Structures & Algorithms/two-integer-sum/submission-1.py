class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num  in enumerate(nums):
            x = target - nums[i]
            if x in d:
                return [d[x], i]
            d[num] = i