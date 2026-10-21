class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles) # rate(k) of eating cannot be more than this 
        res = high 

        # BS to look for k: rate of eating bananas
        while low <= high:
            k = (low + high) // 2 # mid

            # check hrs with this rate (k) -- if its less than given time h
            hrs = 0
            for p in piles: 
                hrs += math.ceil(p / k)
            
            if hrs <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
        
        return res 
