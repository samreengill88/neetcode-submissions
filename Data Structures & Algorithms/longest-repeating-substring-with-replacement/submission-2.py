class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count_map = {}
        l = 0
        res = 0

        for r in range(len(s)):    
            # update count_map of s[r]
            count_map[s[r]] = count_map.get(s[r], 0) + 1

            # to check valid window: len(window) - most freq count ≤ k 
            #                  - if yes, update res to len(window)
            #                  - if not, move l and dec count of l in count_map
            while (r - l + 1) - max(count_map.values()) > k:
                count_map[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res

# n: len(s),  m: unique chars in s 
# TC : for loop runs once for each char - so O(n)
#      while loop to get max: loops through count_map, that is O(m)
#       so O(m * n)
# SC:
        # count_map : O(m) stores unique chars of s