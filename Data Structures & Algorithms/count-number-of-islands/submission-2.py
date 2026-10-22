class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            # base case: if cell out of bound or cell = 0 then return 
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == "0":
                return 
            
            # know: cell = 1 and is in bounds 
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
              
                grid[r][c] = "0"
                dfs(nr, nc)

        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    num_islands += 1
        return num_islands 

# TC: O(m * n) each cell is visited once 
# SC: O(m * n) because of the recursion stack.
