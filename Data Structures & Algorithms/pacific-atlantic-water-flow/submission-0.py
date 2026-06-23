class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs from 
        #   pac: top row  -> 0, (0 to n-1)
        #        left col ->(0 to n-1), 0
        #   atl: right col -> (0 to n-1), (n-1)
        #        bottom row -> (n-1), (0 to n-1)
        # 
        ROWS = len(heights)
        COLS = len(heights[0])

        pac = set()
        atl = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # STEP 3: DFS
        def dfs(r, c, visit, prevHeight):

            # stop when (r, c) is already in visit
            #           (r, c) out of bounds
            #           height < prebHeight since we need height of neighbor to be >= prevHeight

            if ((r, c) in visit) or (r not in range(ROWS)) or (c not in range(COLS)) or (heights[r][c] < prevHeight):
                return 
            
            # know (r, c) not in visit and height satisfies and cell in bounds
            # add (r, c) to visit
            # run dfs on each neighbor
            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])



        # STEP 2: 
        # traversing rows -> cols change -> pac left col and atl right col
        # height of current cell
        for r in range(ROWS):
            # pac left col 
            dfs(r, 0, pac, heights[r][0])

            # atl right col
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        # tranversing cols -> rows change -> pac top row and atl bottom row
        for c in range(COLS):
            # pac top row
            dfs(0, c, pac, heights[0][c])

            # atl bottom row
            dfs(ROWS - 1, c, atl, heights[ROWS - 1] [c])
        ###########



        # STEP 1: if cell both in pac and atl -> add to res 
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
        #####
        