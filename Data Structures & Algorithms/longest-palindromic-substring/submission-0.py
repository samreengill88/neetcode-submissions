class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0

        for i in range(len(s)):
            l = i
            r = i

            # odd len 
            while l >= 0  and r < len(s) and s[l] == s[r]:
                currLen = r - l + 1
                if currLen > length: 
                    res = s[l:r+1]
                    length = max(length, currLen)
                l -= 1
                r += 1
            
            # even len 
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen = r - l + 1
                if currLen > length:
                    res = s[l:r+1]
                    length = max(length, currLen)
                l -= 1
                r += 1
        
        return res
 
            


