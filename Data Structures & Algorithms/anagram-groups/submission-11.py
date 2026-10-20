class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # for each word - count chars #act
        #               word_count = [0] * 26 a->1, c->1, t->1
        # word_count is the key -- add word 
        
        # count_map = {} # does not work if append and key is not there so use default dict
        count_map = defaultdict(list)


        for word in strs: # m: no of strs
            word_count = [0] * 26 
            for char in word: # n: len of longest string
                word_count[ord(char) - ord('a')] += 1
            count_map[tuple(word_count)].append(word)

        return list(count_map.values())
    
    # TC: O(m*n)  
    # SC:  O(m)
    #           if no two words are same, count_map has m strings
    #           counting each word: chars capped at 26 so that's O(1)
    