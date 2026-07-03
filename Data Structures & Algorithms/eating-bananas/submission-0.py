class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
          
        
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            k = (low + high) // 2
            

            hrs = 0
            for p in piles:
                hrs += math.ceil(p / k)
            
            if hrs <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
        
        return res
        
        
        
        
        
        
        
        
        
        # rate = 1

        # while True:
        #     hrs = 0
        #     for p in range(len(piles)):
        #         # calculate hrs per pile
        #         hrs += math.ceil(piles[p] / rate)
        #     if hrs <= h:
        #         return rate
            
        #     rate += 1
        # return rate