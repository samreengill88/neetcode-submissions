class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        
        # borders are never surrounded 
        # run dfs from border O
        #  mark border O  = T
        # change all O = X
        # Change T to O

        ROWS, COLS = len(grid), len(grid[0])
        
        directions = [[1, 0] , [-1, 0], [0, 1], [0, - 1]]

        def dfs(r, c):
            # stop if cell out of bounds or cell is not 0

            if not(r in range(ROWS)) or not(c in range(COLS)) or grid[r][c] != 'O':
                return 


            grid[r][c] = 'T'

            for dr, dc in directions:
                nr, nc = r+ dr, c+dc
                dfs(nr, nc)


        # run dfs on border O's
        for r in range(ROWS):
            if grid[r][0] == 'O':
                dfs(r, 0)
            if grid[r][COLS - 1]== 'O':
                dfs(r, COLS - 1)
        
        for c in range(COLS):
            if grid[0][c] == 'O':
                dfs(0, c)
            if grid[ROWS - 1][c]== 'O':
                dfs(ROWS - 1, c)
        
        

        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'
                if grid[r][c] == 'T':
                    grid[r][c] = 'O'
