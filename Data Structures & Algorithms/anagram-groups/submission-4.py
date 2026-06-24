class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        # res = {}

        for s in strs:
            count = [0] * 26

            # get asci val of that char c in s  -> inc val of c in count for that c
            for char in s:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())