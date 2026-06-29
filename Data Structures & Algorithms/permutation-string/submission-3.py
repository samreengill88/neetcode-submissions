class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # count for s1 - if len s1 = 3
        k = len(s1)
        s1Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
        
        if len(s1) > len(s2):
            return False

        # count for s2
        # count first 3 characters in s2
        s2Count = [0] * 26
        for j in range(len(s1)):
            s2Count[ord(s2[j]) - ord('a')] += 1

        # if both count match 
        if s1Count == s2Count:
            return True


        

        # go through s2 - get first k characters - compare their count with s1Count
        l = 0
        r = k

        while r < len(s2):

            # inc count of r
            s2Count[ord(s2[r]) - ord('a')] += 1

            # dec count of l
            s2Count[ord(s2[l]) - ord('a')] -= 1

            if s1Count == s2Count:
                return True
            
            # does not match
            l += 1
            r += 1
        
        return False
