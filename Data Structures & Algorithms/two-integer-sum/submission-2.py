class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # use hashmap (dictionary)
        hashMap = {}
        for i, n in enumerate(nums): # i is index, n is value at i
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
            
