class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        length = 0
        l = 0
        for char in s:
            
            while char in charSet:
                charSet.remove(s[l])
                l += 1
            if char not in charSet:
                charSet.add(char)
                length = max(length, len(charSet))
            # know: char in set, add all characters until and including char 
            
        
        return length
       