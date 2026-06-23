class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # res = {} 
        # hashMap : [1a, 1c, 1t] : ["act", "cat"]
        res = defaultdict(list) # auto-creates [] for any new key

        for s in strs: # ex: got act
            count = [0] * 26 # count each char like [1a 1c 1t]
            for c in s: # got a
                # increase count of a by 1
                # asci value of a ord(c) - ord("a")
                count[ord(c) - ord("a")] += 1 # got 1a
                # append count to res
            # count is now 1a, 1c, 1t
            
            res[tuple(count)].append(s) 
            # count is lst - mutable so change to tuple - immutable
            # if key dne -> change res to defaultdic
        return list(res.values())

            
