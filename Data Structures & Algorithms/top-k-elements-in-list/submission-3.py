class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # 1: 3
        # 2: 1
        # 3: 5

        for n in nums: 
            count[n] = count.get(n, 0) + 1
        
        # bucket sort 
        # make a lst - index is count, value is num with that count
        freq = [[] for i in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)
        
        # to get top k elements - traverse reverse in freq
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
        

