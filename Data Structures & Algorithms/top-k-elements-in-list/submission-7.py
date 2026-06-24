class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # arr - list of lists
        arr = []
        for i in range(len(nums) + 1):
            arr.append([])
        
       
        # count with hashmap
        # {1: 1, 2: 2, 3: 3, 4:2}
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # put elements in arr using hashmap
        # get freq(f) of each num in hashmap
        # append num in index(f) of arr
        for num in count:
            freq = count[num]
            arr[freq].append(num)
        
        res = []
        # to get top k - lopp through arr - from (n-1) to 0
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res
