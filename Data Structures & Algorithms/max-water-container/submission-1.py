class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # area is calculated as: min(l, r) * abs(l - r)
        # use two pointers: need to find first highest l and second highest r 
        # l = 0
        # r = len(heights) - 1
        # update l to max height
        # update r s.t. 
        #   if r - 1 > r update r to r - 1

        l = 0 
        r = len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * abs(l - r)
            res = max(res, area) # calculating area with different combinations of l and r 
            
            ##### move shorter height by 1 ####
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return res 