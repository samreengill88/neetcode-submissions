class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_lst = []
        for n in nums:
            if n not in new_lst:
                new_lst.append(n)
            
            else:
                return True
        return False