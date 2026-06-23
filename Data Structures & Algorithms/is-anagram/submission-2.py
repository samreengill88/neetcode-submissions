class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26 # a...z

        # char 'a' in s
        #       count[0] += 1
        # char 'a' in t
        #       count[0] -=1
        # at the end if all the values in count are not 0, then not anagram - return False


        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] +=1
            count[ord(t[i]) - ord('a')] -=1
        
        for c in count:
            if c != 0:
                return False
        return True


        # countS = {}
        # countT = {}
        # for i in range(len(s)): 
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)

        # # now check hashmaps if same
        # return countS == countT
        # # for c in countS:
        # #     if countS[c] != countT.get(c, 0):
        # #         return False
        # # return True