class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t = stack.pop()
                stackIndex = t[1]
                res[stackIndex] = i - stackIndex
            stack.append([temp, i])
        
        return res

        