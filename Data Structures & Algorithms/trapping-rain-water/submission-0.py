class Solution:
    def trap(self, height: List[int]) -> int:
        
        # at each index i : area = min(leftMax, rightMax)  - height[i]

        # we can have 3 arrays of size n = len(height):
        #           leftMax
        #           rightMax
        #           min(leftMax, rightMax) - height[i] and sum all

        n = len(height)
        if n == 0:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n
        res = 0

        # leftMax for each index store its leftMax
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(height[i], leftMax[i - 1])
        
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max( height[i], rightMax[i + 1])
        
        for i in range(n):
            area =  min(leftMax[i], rightMax[i]) - height[i]
            if area < 0:
                res += 0
            res += area
        
        
        return res