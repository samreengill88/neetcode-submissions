class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #### need to find rate of eating bananas - use BS ####
        # min rate has to be 1, and max rate can be max(piles)

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

# TC: n: len(piles), m: max(piles) 
#   max(piles) takes O(n)
#   BS in [1, m] - O(log m)
#   inside for loop O(n)
# total: O(n) + log m × O(n) = O(n · log m)

# SC: O(1)