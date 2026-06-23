class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # count: 1 -> 3, 2 -> 1, 100 -> 1
        # 


        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = []
        for i in range(len(nums) + 1):
            freq.append([])
        

        # freq : index represent the count 
        #        values at index represent nums that has count = index
        # [[2, 100], - , [1]]
        # 2 and 100 occurs 1 time, 1 occur 3 times
        for n, c in count.items():
            freq[c].append(n)
        
        # get top k elements from freq, start from end of freq - that has max occuring element
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
