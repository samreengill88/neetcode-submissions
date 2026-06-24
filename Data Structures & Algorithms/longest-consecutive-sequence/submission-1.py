class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # seq starts for n when n - 1 not in nums

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet: # start of the sequence
                length = 1
                # get consecutive numbers for that num
                while (num + length) in numSet:
                    length += 1
                
                longest = max(longest, length)
        return longest