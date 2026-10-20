class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        max_len = 0
        substr_set = set()

        for r in range(len(s)): 
            while s[r] in substr_set:
                substr_set.remove(s[l])
                l += 1

            substr_set.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len