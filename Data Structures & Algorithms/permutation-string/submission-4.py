class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        # 1. count letters in s1
        count_s1 = [0] * 26 
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
        
        window = [0] * 26
        
        l = 0
        # now for s2, start at len(s1)
        for r in range(len(s2)):
            # add r from s2 to window 
            index = ord(s2[r]) - ord('a')
            window[index] += 1
            
            ### if len(window) is greater than len(s1) -> shift l and dec count of l in window
            if (r - l + 1) > len(s1):
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            # if window is same as s1_count -> True
            if window == count_s1:
                return True
        return False
            

            


            

        
       
