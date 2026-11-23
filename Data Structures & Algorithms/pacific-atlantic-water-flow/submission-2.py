class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # pac -> 0 ,       0 to n - 1
        #       0 to n -1, 0 

        # atl -> n - 1,     0 to n - 1
        #       0 to n - 1, n - 1


        def dfs(r, c, visit, prev_height):
            
            # stop if cell out of bounds, cell in visit and 
            # going in to out want prev_height ≥ curr
            # going out to in -> want prev_height ≤ curr
            # stop when prev_height > curr

            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or prev_height > heights[r][c]:
                return  
            
            visit.add((r, c))
            
            # check all neighbors 
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 
                dfs(nr, nc, visit, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])




        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res