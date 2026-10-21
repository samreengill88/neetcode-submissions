class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [] # It holds index of days that haven’t found a warmer day yet.

        for i, t in enumerate(temperatures):
            # if stack is not empty and t is greater than top temp in stack then update res
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
    
    # TC: O(n)
    # SC: worst case all dec temperatures no day finds warmers one [90, 80, 70, 60]
    #       - so stack holds all n indices
    #       - so O(n)