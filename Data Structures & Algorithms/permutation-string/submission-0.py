class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # count for s1
        k = len(s1)
        s1Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
        
        l = 0

        # go through s2 - get first k characters - compare their count with s1Count
        
        r = k - 1

        while r < len(s2):
            # get count of this window
            s2Count = [0] * 26
            for j in range(l, r + 1):
                # index of char in s2 - its ord - ord of a 
                s2Count[ord(s2[j]) - ord('a')] += 1

            if s1Count == s2Count:
                return True
            
            # does not match
            l += 1
            r += 1
        
        return False
