class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        longest_seq = 0
        for n in nums:
            
            if (n - 1) not in nums:
                # it is a start of sequence
                length = 1

                # get consecutive nums if present
                while (n + length) in nums:
                    length += 1

                longest_seq = max(length, longest_seq)
        
        return longest_seq

    # TC: O(n)
    #   - while loop runs only for start of sequence , each num belongs to exactly one seq

    # SC: O(n) 
    #   - no sequence: [10, 5, 3, 8, 1] 