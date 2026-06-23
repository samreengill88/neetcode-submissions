import collections

class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
        
        # # empty grid
        # if not grid:
        #     return 0
        
        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # islands = 0


        # # bfs
        # def bfs(r, c):
        #     q = collections.deque()
        #     q.append((r, c))
        #     visited.add((r, c))

        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if (r in range(rows) and
        #                 c in range(cols) and
        #                 grid[r][c] == "1" and 
        #                 (r, c) not in visited 
        #             ):
        #                 q.append((r, c))
        #                 visited.add((r, c))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r, c) not in visited:
        #             bfs(r, c)
        #             islands +=1
        # return islands
    
    # dfs
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r,c):
            # if cell out of bounds or cell == "0" - return
            if (r not in range(ROWS)) or (c not in range(COLS)) or grid[r][c] == "0":
                return
            # know cell is in bounds and cell == "1" so run dfs on neighbour
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                grid[r][c] = "0"
                dfs(nr, nc)



        for r in range(ROWS):
            for c in range(COLS):
                # if its land - run dfs
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        
        return res

