class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # using dfs 
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0 
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            # base case: if cell out of bounds or cell is 0 -> return 
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area

# TC: O(m * n)
# SC: O(m * n)