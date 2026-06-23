class Solution:
    def myPow(self, x: float, n: int) -> float:
        if  x == 0:
            return 0 
        elif n == 0:
            return 1
        else:
            # x = 2, n = 10
            res = 1
            for i in range (abs(n)):
                res *= x
            if n >= 0: # power is +ve 
                return res
            else:    # power is -ve
                return 1 / res 

                 