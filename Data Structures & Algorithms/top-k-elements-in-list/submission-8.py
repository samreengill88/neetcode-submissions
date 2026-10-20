class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # each index is empty list 
        # index:count 
        # values: [ ] -- nums with that count
        word_count_lst = [[] for i in range(len(nums) + 1)]

        count_map = {} # num -> count
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        
        # traverse count_map and update word_count_lst
        for num, count in count_map.items():
            word_count_lst[count].append(num)
        
        res = []
        for i in range(len(word_count_lst) - 1, -1, -1):
            for num in word_count_lst[i]:
                if len(res) == k:
                    return res
                res.append(num)
        
        return res