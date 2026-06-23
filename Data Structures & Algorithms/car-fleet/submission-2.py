class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []

        for i in range(len(position)):
            pair.append((position[i], speed[i]))
        
        pair.sort(reverse=True)

        stack = []

        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()   
        
        return len(stack)