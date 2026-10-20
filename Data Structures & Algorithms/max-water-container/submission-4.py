class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        j = len(heights) - 1
        max_height = 0 
        
        while i < j:
            length = abs(j - i) # 7
            height = min(heights[i], heights[j])
            area = length * height
            max_height = max(max_height, area)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_height

# TC: O(n)
# SC: O(1)
